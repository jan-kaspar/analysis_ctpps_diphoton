#include "TFile.h"
#include "TH1D.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TSpline.h"

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
#include <map>

//----------------------------------------------------------------------------------------------------

using namespace std;
using namespace edm;

#include "input_files.h"

#include "shared_track.h"
#include "shared_alignment.h"
#include "shared_reconstruction.h"
#include "shared_fill_info.h"

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

//----------------------------------------------------------------------------------------------------

struct EventInfo
{
	unsigned int lumisection = 0;

	double dp_mass = 0.;
	double dp_y = 0.;
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
		// TODO
		int ir = fscanf(f, "%u:%u:%lu %lf %lf", &k.run, &i.lumisection, &k.event, &i.dp_mass, &i.dp_y);
		//int ir = fscanf(f, "%u:%u:%lu %lf", &k.run, &i.lumisection, &k.event, &i.dp_mass);

		// TODO
		if (ir == 5)
		//if (ir == 4)
			eventInfo[k] = i;

		if (ir == 0)
		{
			printf("ERROR: ir = %i\n", ir);
			break;
		}
	}

	fclose(f);

	/*
	printf("<<<\n");
	for (auto &p : eventInfo)
	{
		printf("%u:%lu => %u, %.1f, %.2f\n", p.first.run, p.first.event, p.second.lumisection, p.second.dp_mass, p.second.dp_y);
	}
	printf(">>>\n");
	*/
}

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
	
	InitReconstruction();
	InitFillInfoCollection();

	AlignmentResultsCollection alignment;
	if (alignment.Load("../alignment/alignment_collection.out") != 0)
	{
		printf("ERROR: can't load alignment data.\n");
		return 10;
	}

	// prepare ouput
	TFile *f_out = new TFile("distributions.root", "recreate");

	// book histograms
	TH1D *h_dp_mass = new TH1D("h_dp_mass", ";diphoton mass", 20, 500., 2000.);
	TH1D *h_dp_mass_tr_both_arms = new TH1D("h_dp_mass_tr_both_arms", ";diphoton mass", 20, 500., 2000.);

	TH1D *h_xi_L = new TH1D("h_xi_L", ";#xi_{L}", 25, 0., 0.25);
	TH1D *h_xi_R = new TH1D("h_xi_R", ";#xi_{R}", 25, 0., 0.25);
	TH1D *h_m = new TH1D("h_m", ";mass	 (GeV)", 20, 0., 2000.);
	TH1D *h_y = new TH1D("h_y", ";rapidity", 20, -0.5, 1.0);
	
	TGraph *g_event_vs_run = new TGraph(); g_event_vs_run->SetName("g_event_vs_run"); g_event_vs_run->SetTitle(";run;candidate idx");

	TH1D *h_m_diff_RP_CMS = new TH1D("h_m_diff_RP_CMS", ";m_{RP} - m_{CMS}", 50, -1000., +1000.);
	TGraphErrors *g_m_RP_vs_m_CMS = new TGraphErrors(); g_m_RP_vs_m_CMS->SetName("g_m_RP_vs_m_CMS"); g_m_RP_vs_m_CMS->SetTitle(";m_{CMS};m_{RP}");

	TH1D *h_y_diff_RP_CMS = new TH1D("h_y_diff_RP_CMS", ";y_{RP} - y_{CMS}", 50, -5., +5.);
	TGraphErrors *g_y_RP_vs_y_CMS = new TGraphErrors(); g_y_RP_vs_y_CMS->SetName("g_y_RP_vs_y_CMS"); g_y_RP_vs_y_CMS->SetTitle(";y_{CMS};y_{RP}");

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
		} else {
			printf("WARNING: no event info for run:event = %u:%llu\n", event.id().run(), event.id().event());
		}

		// get track data for horizontal RPs
		TrackDataCollection trackData_raw;
		for (const auto &ds : *tracks)
		{
			const auto &rpId = ds.detId();
			for (const auto &t : ds)
			{
				if (rpId == 3 || rpId == 2 || rpId == 102 || rpId == 103)
					trackData_raw[rpId] = t;
			}
		}

		// apply alignment corrections
		const auto &fillInfo = fillInfoCollection.FindByRun(event.id().run());
		const auto alignment_it = alignment.find(fillInfo.alignmentTag);
		if (alignment_it == alignment.end())
		{
			printf("ERROR: no alignment for tag '%s'.\n", fillInfo.alignmentTag.c_str());
			return 1;
		}
		TrackDataCollection trackData_al = alignment_it->second.Apply(trackData_raw);

		// split track collection per arm
		TrackDataCollection trackData_L, trackData_R;
		for (const auto &p : trackData_al)
		{
			int arm = p.first / 100;
			if (arm == 0)
				trackData_L[p.first] = p.second;
			if (arm == 1)
				trackData_R[p.first] = p.second;
		}

		// run recontruction in each arm
		ProtonData proton_L = ReconstructProton(trackData_L, true);
		ProtonData proton_R = ReconstructProton(trackData_R, false);

		// mass calculation etc.
		if (proton_L.valid && proton_R.valid)
		{
			double W = 13000.;	// sqrt(s) in GeV

			double m = W * sqrt(proton_L.xi * proton_R.xi);
			double m_unc = m / 2. * sqrt( pow(proton_L.xi_unc / proton_L.xi, 2.) + pow(proton_R.xi_unc / proton_R.xi, 2.) );

			double y = 1./2. * log(proton_R.xi / proton_L.xi);
			double y_unc = 1. / 2. * sqrt( pow(proton_L.xi_unc / proton_L.xi, 2.) + pow(proton_R.xi_unc / proton_R.xi, 2.) );

			h_xi_L->Fill(proton_L.xi);
			h_xi_R->Fill(proton_R.xi);

			h_m->Fill(m);
			h_y->Fill(y);

			if (it != eventInfo.end())
			{
				const auto &ei = it->second;

				int idx = g_event_vs_run->GetN();
				
				g_event_vs_run->SetPoint(idx, event.id().run(), event.id().event());

				g_m_RP_vs_m_CMS->SetPoint(idx, ei.dp_mass, m);
				g_m_RP_vs_m_CMS->SetPointError(idx, 0., m_unc);

				h_m_diff_RP_CMS->Fill(m - ei.dp_mass);

				g_y_RP_vs_y_CMS->SetPoint(idx, ei.dp_y, y);
				g_y_RP_vs_y_CMS->SetPointError(idx, 0., y_unc);

				h_y_diff_RP_CMS->Fill(y - ei.dp_y);

				printf("CORRELATION: run %u, event %llu\n", event.id().run(), event.id().event());
				printf("\tdi-photon: mass = %.3f, y = %.3f\n", ei.dp_mass, ei.dp_y);
				printf("\tRP: xi_L = %.3f +- %.3f, xi_R = %.3f +- %.3f, mass = %.3f +- %.3f, RP y = %.3f +- %.3f\n",
					proton_L.xi, proton_L.xi_unc, proton_R.xi, proton_R.xi_unc, m, m_unc, y, y_unc);
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

	g_event_vs_run->Write();

	h_m_diff_RP_CMS->Write();
	g_m_RP_vs_m_CMS->Write();

	h_y_diff_RP_CMS->Write();
	g_y_RP_vs_y_CMS->Write();

	// clean up
	delete f_out;
	return 0;
}
