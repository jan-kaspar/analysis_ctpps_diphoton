#include "input_files.h"

#include "TFile.h"
#include "TH1D.h"
#include "TGraph.h"
#include "TGraphErrors.h"

#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/ChainEvent.h"

#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/CTPPSReco/interface/TotemRPLocalTrack.h"
#include "DataFormats/CTPPSReco/interface/TotemRPUVPattern.h"
#include "DataFormats/CTPPSReco/interface/TotemRPCluster.h"
#include "DataFormats/TotemDigi/interface/TotemRPDigi.h"
#include "DataFormats/TotemDigi/interface/TotemVFATStatus.h"
#include "DataFormats/TotemRPDetId/interface/TotemRPDetId.h"

#include <vector>
#include <string>

//----------------------------------------------------------------------------------------------------

using namespace std;
using namespace edm;

//----------------------------------------------------------------------------------------------------

// defaults
string event_info_file = "";

#include "parameters.h"

//----------------------------------------------------------------------------------------------------

struct EventKey
{
	unsigned int run;
	unsigned long event;

	bool operator< (const EventKey &other) const
	{
		if (run < other.run)
			return true;

		if (run > other.run)
			return false;

		if (event < other.event)
			return true;

		return false;
	}
};

struct EventInfo
{
	unsigned int lumisection;
	double dp_mass;
};

map<EventKey, EventInfo> eventInfo;

//----------------------------------------------------------------------------------------------------

void LoadEventInfo(const string &fn)
{
	FILE *f = fopen(fn.c_str(), "r");

	while (!feof(f))
	{
		EventKey k;
		EventInfo i;
		int ir = fscanf(f, "%u:%u:%lu %lf", &k.run, &i.lumisection, &k.event, &i.dp_mass);

		if (ir == 4)
			eventInfo[k] = i;

		if (ir == 0)
		{
			printf("ERROR: ir = %i\n", ir);
			break;
		}
	}

	fclose(f);

	/*
	for (auto &p : eventInfo)
	{
		printf("%u:%lu => %u, %.1f\n", p.first.run, p.first.event, p.second.lumisection, p.second.dp_mass);
	}
	*/
}

//----------------------------------------------------------------------------------------------------

struct TrackData
{
	bool valid = false;
	double x = 0.;
	double y = 0.;

	void operator= (const TotemRPLocalTrack &ft)
	{
		valid = ft.isValid();
		x = ft.getX0();
		y = ft.getY0();
	}
};

//----------------------------------------------------------------------------------------------------
//----------------------------------------------------------------------------------------------------

int main()
{
	// apply settings
	ApplySettings();

	// prepare input
	LoadEventInfo(event_info_file);

	InitInputFiles();
	fwlite::ChainEvent event(input_files);

	// prepare ouput
	TFile *f_out = new TFile("distributions.root", "recreate");

	// book histograms
	TH1D *h_dp_mass = new TH1D("h_dp_mass", ";diphoton mass", 20, 500., 2000.);
	TH1D *h_dp_mass_tr_both_arms = new TH1D("h_dp_mass_tr_both_arms", ";diphoton mass", 20, 500., 2000.);

	TH1D *h_xi_L = new TH1D("h_xi_L", ";#xi_{L}", 25, 0., 0.25);
	TH1D *h_xi_R = new TH1D("h_xi_R", ";#xi_{R}", 25, 0., 0.25);
	TH1D *h_m = new TH1D("h_m", ";mass	 (GeV)", 20, 0., 2000.);
	TH1D *h_y = new TH1D("h_y", ";rapidity", 20, -0.5, 1.0);

	TGraphErrors *g_m_RP_vs_m_CMS = new TGraphErrors(); g_m_RP_vs_m_CMS->SetName("g_m_RP_vs_m_CMS"); g_m_RP_vs_m_CMS->SetTitle(";m_{CMS};m_{RP}");

	// init counters
	unsigned int N=0;
	unsigned int N_L_any=0, N_L_one=0, N_L_two=0;
	unsigned int N_R_any=0, N_R_one=0, N_R_two=0;
	unsigned int N_LR=0;

	// before looping
	printf("run, event, 45-F, 45-N, 56-N, 56-F\n");

	// loop over the chain entries
	for (event.toBegin(); ! event.atEnd(); ++event)
	{
		fwlite::Handle< DetSetVector<TotemRPLocalTrack> > tracks;
		tracks.getByLabel(event, "totemRPLocalTrackFitter");
	
		map<unsigned int, bool> tr;
		tr[2] = false;
		tr[3] = false;
		tr[102] = false;
		tr[103] = false;
	
		for (const auto &ds : *tracks)
		{
			for (const auto &t : ds)
			{
				if (t.isValid())
				{
					tr[ds.detId()] = true;
				}
			}
		}
		
		printf("%u, %llu, %i, %i, %i, %i\n", event.id().run(), event.id().event(),
				tr[3], tr[2], tr[102], tr[103]
			);
	
		N++;
	
		if (tr[2] || tr[3])
			N_L_any++;
		if ( (tr[2] || tr[3]) && !(tr[2] && tr[3]))
			N_L_one++;
		if (tr[2] && tr[3])
			N_L_two++;
	
		if (tr[102] || tr[103])
			N_R_any++;
		if ( (tr[102] || tr[103]) && !(tr[102] && tr[103]))
			N_R_one++;
		if (tr[102] && tr[103])
			N_R_two++;
	
		bool track_both_arms = (tr[2] || tr[3]) && (tr[102] || tr[103]);
		if (track_both_arms)
			N_LR++;

		// get event info
		EventKey ek{event.id().run(), event.id().event()};
		const auto &it = eventInfo.find(ek);
		if (it != eventInfo.end())
		{
			const auto &ei = it->second;

			h_dp_mass->Fill(ei.dp_mass);

			if (track_both_arms)
				h_dp_mass_tr_both_arms->Fill(ei.dp_mass);
		}

		// get track data for horizontal RPs
		TrackData tr_L_1_F;
		TrackData tr_L_1_N;
		TrackData tr_R_1_N;
		TrackData tr_R_1_F;

		for (const auto &ds : *tracks)
		{
			const auto &rpId = ds.detId();

			for (const auto &t : ds)
			{
				if (rpId == 3)
					tr_L_1_F = t;
				if (rpId == 2)
					tr_L_1_N = t;
				if (rpId == 102)
					tr_R_1_N = t;
				if (rpId == 103)
					tr_R_1_F = t;
			}
		}

		// alignment corrections
		double de_x_L_1_F, de_x_L_1_N, de_x_R_1_N, de_x_R_1_F;	// in mm
		if (event.id().run() < 274244)
		{
			de_x_L_1_F = -3.40;
			de_x_L_1_N = -0.90;
			de_x_R_1_N = -2.75;
			de_x_R_1_F = -2.40;
		} else {
			de_x_L_1_F = -3.90;
			de_x_L_1_N = -1.45;
			de_x_R_1_N = -3.25;
			de_x_R_1_F = -2.85;
		}

		// optics
		double D_L_1_F = 9.22E-02;	// in m
		double D_L_1_N = 9.26E-02;
		double D_R_1_N = 5.81E-02;
		double D_R_1_F = 5.16E-02;

		// simple proton reconstruction
		if (tr_L_1_F.valid && tr_R_1_F.valid)
		{
			double x_L_1_F = tr_L_1_F.x + de_x_L_1_F;
			double x_R_1_F = tr_R_1_F.x + de_x_R_1_F;

			double xi_L_1_F = x_L_1_F*1E-3 / D_L_1_F;
			double xi_R_1_F = x_R_1_F*1E-3 / D_R_1_F;

			double de_x = 0.2E-3;	// m
			double de_rel_D = 0.1;	// 1

			double xi_L_1_F_unc = sqrt( pow(de_x / D_L_1_F, 2.) + pow(de_rel_D * xi_L_1_F, 2.) );
			double xi_R_1_F_unc = sqrt( pow(de_x / D_R_1_F, 2.) + pow(de_rel_D * xi_R_1_F, 2.) );

			double W = 13000.;	// sqrt(s) in GeV

			double m = W * sqrt(xi_L_1_F * xi_R_1_F);
			double m_unc = m / 2. * sqrt( pow(xi_L_1_F_unc / xi_L_1_F, 2.) + pow(xi_R_1_F_unc / xi_R_1_F, 2.) );

			double y = 1./2. * log(xi_R_1_F / xi_L_1_F);
			double y_unc = 1. / 2. * sqrt( pow(xi_L_1_F_unc / xi_L_1_F, 2.) + pow(xi_R_1_F_unc / xi_R_1_F, 2.) );

			h_xi_L->Fill(xi_L_1_F);
			h_xi_R->Fill(xi_R_1_F);

			h_m->Fill(m);
			h_y->Fill(y);
		
			if (it != eventInfo.end())
			{
				const auto &ei = it->second;

				int idx = g_m_RP_vs_m_CMS->GetN();

				g_m_RP_vs_m_CMS->SetPoint(idx, ei.dp_mass, m);
				g_m_RP_vs_m_CMS->SetPointError(idx, 0., m_unc);

				printf("correlation: run %u, event %llu, di-photon mass = %.3f, RP mass = %.3f +- %.3f, RP y = %.3f +- %.3f\n",
					event.id().run(), event.id().event(), ei.dp_mass, m, m_unc, y, y_unc);
			} else {
				printf("WARNING: no event info for run:event = %u:%llu\n", event.id().run(), event.id().event());
			}
		}
	}

	// print counters
	printf("\n");

	printf("events analyzed, %u\n", N);
	printf("\n");

	double Nd = N;
	
	printf("left arm: track in any RP, %.3f\n", N_L_any / Nd);
	printf("left arm: track in one RP, %.3f\n", N_L_one / Nd);
	printf("left arm: track in two RP, %.3f\n", N_L_two / Nd);

	printf("\n");

	printf("right arm: track in any RP, %.3f\n", N_R_any / Nd);
	printf("right arm: track in one RP, %.3f\n", N_R_one / Nd);
	printf("right arm: track in two RP, %.3f\n", N_R_two / Nd);

	printf("\n");

	printf("tracks in both arms, %.3f\n", N_LR / Nd);

	// save histograms
	gDirectory = f_out;

	h_dp_mass->Write();
	h_dp_mass_tr_both_arms->Write();

	h_xi_L->Write();
	h_xi_R->Write();
	h_m->Write();
	h_y->Write();

	g_m_RP_vs_m_CMS->Write();

	// clean up
	delete f_out;
	return 0;
}
