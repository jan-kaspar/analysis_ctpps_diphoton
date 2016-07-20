void InitReconstruction()
{
}

//----------------------------------------------------------------------------------------------------

void ReconstructFromOneRP(const map<unsigned int, TrackData> &tracks, unsigned int id, double D, ProtonData &result)
{
	result.valid = false;

	auto it = tracks.find(id);
	if (it == tracks.end())
		return;
	
	const auto &tr = it->second;

	if (!tr.valid)
		return;

	result.valid = true;

	result.xi = tr.x*1E-3 / D;

	double de_x = 0.2E-3;	// m
	double de_rel_D = 0.1;	// 1

	result.xi_unc = sqrt( pow(de_x / D, 2.) + pow(de_rel_D * result.xi, 2.) );
}

//----------------------------------------------------------------------------------------------------

ProtonData ReconstructProton(const map<unsigned int, TrackData> &tracks, bool leftArm)
{
	ProtonData result;
	result.valid = false;

	double D_1_F, D_1_N; // in mm
	unsigned int id_1_F, id_1_N;

	if (leftArm)
	{
		D_1_N = 9.26E-02;
		D_1_F = 9.22E-02;

		id_1_N = 2;
		id_1_F = 3;
	} else {
		D_1_N = 5.81E-02;
		D_1_F = 5.16E-02;

		id_1_N = 102;
		id_1_F = 103;
	}

	// try far
	ReconstructFromOneRP(tracks, id_1_F, D_1_F, result);

	// if far not successfull, try near
	if (!result.valid)
		ReconstructFromOneRP(tracks, id_1_N, D_1_N, result);

	return result;
}
