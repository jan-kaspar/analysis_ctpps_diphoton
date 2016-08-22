import root;
import pad_layout;

string topDir = "../../";

string datasets[] = { "EE", "EB" };

xSizeDef = 10cm;
ySizeDef = 8cm;

//xTicksDef = LeftTicks(100., 50.);

//----------------------------------------------------------------------------------------------------

for (string dataset : datasets)
{
	NewPad(false);
	label("{\SetFontSizesXX " + dataset + "}");
}

NewRow();

/*
for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$\xi$");
	currentpad.xTicks = LeftTicks(0.05, 0.01);

	draw(RootGetObject(f, "h_xi_L"), "vl", blue+2pt, "left arm");
	draw(RootGetObject(f, "h_xi_R"), "vl", red+2pt, "right arm");
	xlimits(0, 0.25, Crop);

	AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{\rm RP}\ung{GeV}$");
	currentpad.xTicks = LeftTicks(500., 100.);

	draw(RootGetObject(f, "h_m"), "vl", magenta+2pt);
	xlimits(0, 2000, Crop);

	//AttachLegend();
}

NewRow();
*/

TGraph_errorBar = None;

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{\rm CMS}\ung{GeV}$", "$m_{\rm RP}\ung{GeV}$");
	currentpad.xTicks = LeftTicks(500., 100.);
	currentpad.yTicks = RightTicks(500., 100.);

	draw((0, 0)--(2000, 2000), dashed);
	RootObject g_mass = RootGetObject(f, "g_m_RP_vs_m_CMS");
	draw(g_mass, "p", heavygreen, mCi+3pt+heavygreen);
	limits((0, 0), (2000, 2000));
	
	RootObject g_cand = RootGetObject(f, "g_event_vs_run");

	int N = robj.iExec("GetN");
	for (int i = 0; i < N; ++i)
	{
		real ax[] = {0.};
		real ay[] = {0.};

		g_mass.vExec("GetPoint", i, ax, ay);
		real x = ax[0], y = ay[0];

		g_cand.vExec("GetPoint", i, ax, ay);
		int run = (int) ax[0], event = (int) ay[0];
		
		label(format("%i", (run % 10000)) + format(":%i", (event % 1000)), (x, y), E, heavygreen);
	}

	//AttachLegend();
}

/*
NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";

	NewPad("$m_{\rm RP} - m_{\rm CMS} \ung{GeV}$");
	currentpad.xTicks = LeftTicks(500., 100.);

	RootGetObject(f, "h_m_diff_RP_CMS");
	draw(robj, "vl", black+2pt);

	AttachLegend();
}
*/

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";

	NewPad("diphoton mass$\ung{GeV}$");

	RootGetObject(f, "h_dp_mass");
	draw(robj, "vl", blue+2pt, format("diphoton cut (%.0f events)", robj.rExec("GetEntries")));

	RootGetObject(f, "h_dp_mass_tr_both_arms");
	draw(robj, "vl", red+2pt, format("diphoton cut, RP tracks L \& R (%.0f events)", robj.rExec("GetEntries")));
	
	AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$y_{\rm RP}\ung{GeV}$");
	draw(RootGetObject(f, "h_y"), "vl", brown+2pt);
	xlimits(-0.5, 1.0, Crop);

	//AttachLegend();
}

/*
NewRow();

TGraph_errorBar = None;

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$y_{\rm CMS}$", "$y_{\rm RP}$");
	//currentpad.xTicks = LeftTicks(500., 100.);
	//currentpad.yTicks = RightTicks(500., 100.);

	//draw((0, 0)--(2000, 2000), dashed);
	RootObject g_y = RootGetObject(f, "g_y_RP_vs_y_CMS");
	draw(g_y, "p", heavygreen, mCi+3pt+heavygreen);
	//limits((0, 0), (2000, 2000));
	
	RootObject g_cand = RootGetObject(f, "g_event_vs_run");

	int N = robj.iExec("GetN");
	for (int i = 0; i < N; ++i)
	{
		real ax[] = {0.};
		real ay[] = {0.};

		g_y.vExec("GetPoint", i, ax, ay);
		real x = ax[0], y = ay[0];

		g_cand.vExec("GetPoint", i, ax, ay);
		int run = (int) ax[0], event = (int) ay[0];
		
		label(format("%i", (run % 10000)) + format(":%i", (event % 1000)), (x, y), E, heavygreen);
	}

	//AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";

	NewPad("$y_{\rm RP} - y_{\rm CMS}$");
	//currentpad.xTicks = LeftTicks(500., 100.);

	RootGetObject(f, "h_y_diff_RP_CMS");
	draw(robj, "vl", black+2pt);

	AttachLegend();
}
*/
