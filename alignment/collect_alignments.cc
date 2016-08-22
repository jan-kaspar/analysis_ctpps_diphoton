#include "../shared_track.h"
#include "../shared_alignment.h"

int main()
{
	vector<string> input_dirs = {
		"margin/fill_4947",
		"margin/fill_4953",
		"margin/fill_4961",
		"margin/fill_4964",
		"margin/fill_4976",

		"no_margin/fill_4964",
		"no_margin/fill_4985",
		"no_margin/fill_4988",
		"no_margin/fill_4990",
		"no_margin/fill_5005",
		"no_margin/fill_5013",
		"no_margin/fill_5017",
		"no_margin/fill_5020",
		"no_margin/fill_5021",
		"no_margin/fill_5024",
		"no_margin/fill_5026",
		"no_margin/fill_5027",
		"no_margin/fill_5028",
		"no_margin/fill_5029",
		"no_margin/fill_5030",
		"no_margin/fill_5038",
		"no_margin/fill_5043",
		"no_margin/fill_5045",
		"no_margin/fill_5048",
		"no_margin/fill_5052",
	};
	
	AlignmentResultsCollection output;

	for (const auto dir : input_dirs)
	{
		AlignmentResultsCollection input;
		int error = input.Load("../../alignment/run_physics_" + dir + "/match.out");
		if (error != 0)
		{
			printf("ERROR: can't load alignment results from directory '%s'.\n", dir.c_str());
			continue;
		}

		auto it = input.find("method x");

		if (it == input.end())
		{
			printf("ERROR: can't get result 'method x' from directory '%s'.\n", dir.c_str());
			continue;
		}

		output[dir + "/method x"] = it->second;
	}

	output.Write("alignment_collection.out");

	return 0;
}
