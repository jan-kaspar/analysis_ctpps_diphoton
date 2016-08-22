struct TrackData
{
	bool valid = false;
	double x = 0.;	// mm
	double y = 0.;	// mm

	void operator= (const TotemRPLocalTrack &ft)
	{
		valid = ft.isValid();
		x = ft.getX0();
		y = ft.getY0();
	}
};

//----------------------------------------------------------------------------------------------------

struct ProtonData
{
	bool valid = false;

	double vtx_x = 0., vtx_y = 0.;	// m

	double th_x = 0., th_y = 0.;	// rad

	double xi = 0.;					// 1, positive when energy loss
	double xi_unc = 0.;
};
