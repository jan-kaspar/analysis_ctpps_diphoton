map<unsigned int, TrackData> ApplyAlignment(unsigned int run, const map<unsigned int, TrackData> &input)
{
	map<unsigned int, TrackData> output = input;

	if (run < 274244)
	{
		output[3].x   += -3.40;
		output[2].x   += -0.90;
		output[102].x += -2.75;
		output[103].x += -2.40;
	} else {
		output[3].x   += -3.90;
		output[2].x   += -1.45;
		output[102].x += -3.25;
		output[103].x += -2.85;
	}

	return output;
}

//----------------------------------------------------------------------------------------------------
