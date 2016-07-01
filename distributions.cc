#include "input_files.h"

#include "TFile.h"
#include "TH1D.h"

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

	for (auto &p : eventInfo)
	{
		printf("%u:%lu => %u, %.1f\n", p.first.run, p.first.event, p.second.lumisection, p.second.dp_mass);
	}
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

	// prepare ouput
	TFile *f_out = new TFile("distributions.root", "recreate");

	// book histograms
	TH1D *h_dp_mass = new TH1D("h_dp_mass", ";diphoton mass", 20, 500., 1200.);
	TH1D *h_dp_mass_tr_both_arms = new TH1D("h_dp_mass_tr_both_arms", ";diphoton mass", 20, 500., 1200.);

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

	// clean up
	delete f_out;
	return 0;
}
