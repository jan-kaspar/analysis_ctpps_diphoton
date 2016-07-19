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

	auto it = tracks.find(id_1_F);
	if (it == tracks.end())
		return result;

	const auto &tr = it->second;

	if (tr.valid == false)
		return result;

	result.valid = true;

	result.xi = tr.x*1E-3 / D_1_F;

	double de_x = 0.2E-3;	// m
	double de_rel_D = 0.1;	// 1

	result.xi_unc = sqrt( pow(de_x / D_1_F, 2.) + pow(de_rel_D * result.xi, 2.) );

	return result;
}
