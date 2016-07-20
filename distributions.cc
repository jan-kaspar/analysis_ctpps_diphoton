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
#include <map>

//----------------------------------------------------------------------------------------------------

using namespace std;
using namespace edm;

#include "input_files.h"

#include "common.h"
#include "alignment.h"
#include "reconstruction.h"

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
//----------------------------------------------------------------------------------------------------

int main()
{
	// apply settings
	ApplySettings();

	// prepare input
	LoadEventInfo(event_info_file);

	InitInputFiles();
	fwlite::ChainEvent event(input_files);
	
	InitAlignment();
	InitReconstruction();

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

	TGraph *g_candidate_vs_run = new TGraph(); g_candidate_vs_run->SetName("g_candidate_vs_run"); g_candidate_vs_run->SetTitle(";run;candidate idx");

	// init counters
	unsigned int N=0;
	unsigned int N_L_any=0, N_L_one=0, N_L_two=0;
	unsigned int N_R_any=0, N_R_one=0, N_R_two=0;
	unsigned int N_LR=0;

	// before looping
	printf("run, event, 45-F, 45-N, 56-N, 56-F\n");

	// loop over the chain entries
	map<unsigned int, unsigned int> candidatesPerRun;

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
		map<unsigned int, TrackData> trackData_raw;
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
		map<unsigned int, TrackData> trackData_al = ApplyAlignment(event.id().run(), trackData_raw);

		// split track collection per arm
		map<unsigned int, TrackData> trackData_L, trackData_R;
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

			auto cit = candidatesPerRun.find(event.id().run());
			if (cit == candidatesPerRun.end())
				cit = candidatesPerRun.insert({event.id().run(), 0}).first;
		
			if (it != eventInfo.end())
			{
				const auto &ei = it->second;

				int idx = g_m_RP_vs_m_CMS->GetN();

				g_m_RP_vs_m_CMS->SetPoint(idx, ei.dp_mass, m);
				g_m_RP_vs_m_CMS->SetPointError(idx, 0., m_unc);

				g_candidate_vs_run->SetPoint(idx, event.id().run(), cit->second);
				cit->second++;

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
	g_candidate_vs_run->Write();

	// clean up
	delete f_out;
	return 0;
}
