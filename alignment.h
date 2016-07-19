void ApplyAlignment(unsigned int run, map<unsigned int, TrackData> &tr)
{
	if (run < 274244)
	{
		tr[3].x += -3.40;
		tr[2].x += -0.90;
		tr[102].x += -2.75;
		tr[103].x += -2.40;
	} else {
		tr[3].x += -3.90;
		tr[2].x += -1.45;
		tr[102].x += -3.25;
		tr[103].x += -2.85;
	}
}

//----------------------------------------------------------------------------------------------------
