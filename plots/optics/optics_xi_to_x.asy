import root;
import pad_layout;

string topDir = "../../";

string rps[] = {
	"L_1_F",
	"L_1_N",
	"R_1_N",
	"R_1_F"
};

xSizeDef = 8cm;

//----------------------------------------------------------------------------------------------------

string f = topDir + "optics.root";

NewPad("$x\ung{m}$", "$\xi$");
for (int rpi : rps.keys)
{
	pen p = StdPen(rpi);
	string l = replace(rps[rpi], "_", "\_");
	draw(RootGetObject(f, "g_x_to_xi_" + rps[rpi]), "l", p, l);
}

AttachLegend(SE, SE);
