#include "TFile.h"
#include "TGraph.h"
#include "TSpline.h"

#include <string>

using namespace std;

//----------------------------------------------------------------------------------------------------

void ProcessOne(TFile *f_in, const string &obj_in, TFile *f_out, const string &obj_out)
{
	// get input
	TGraph *g_in = (TGraph *) f_in->Get(obj_in.c_str());
	if (g_in == NULL)
	{
		printf("ERROR in ProcessOne > g_in = NULL.\n");
		return;
	}

	// determine offset
	double offset = g_in->GetX()[0];

	// preprare output
	TGraph *g_out = new TGraph;
	g_out->SetName(("g_" + obj_out).c_str());
	g_out->SetTitle(";x   (m);#xi");

	// build output
	for (int i = 0; i < g_in->GetN(); ++i)
	{
		double x, y;
		g_in->GetPoint(i, x, y);

		g_out->SetPoint(i, x - offset, -y);
	}

	TSpline3 *s_out = new TSpline3("", g_out->GetX(), g_out->GetY(), g_out->GetN());
	s_out->SetName(("s_" + obj_out).c_str());

	// save ouput
	gDirectory = f_out;
	g_out->Write();
	s_out->Write();
}

//----------------------------------------------------------------------------------------------------

int main()
{
	TFile *f_in_beam1 = TFile::Open("xi_as_a_function_of_x_graph_b1.root");
	TFile *f_in_beam2 = TFile::Open("xi_as_a_function_of_x_graph_b2.root");
	
	TFile *f_out = TFile::Open("optics.root", "recreate");

	ProcessOne(f_in_beam1, "XRPH_C6R5_B1", f_out, "x_to_xi_R_1_N");
	ProcessOne(f_in_beam1, "XRPH_D6R5_B1", f_out, "x_to_xi_R_1_F");

	ProcessOne(f_in_beam2, "XRPH_C6L5_B2", f_out, "x_to_xi_L_1_N");
	ProcessOne(f_in_beam2, "XRPH_D6L5_B2", f_out, "x_to_xi_L_1_F");

	delete f_out;
	delete f_in_beam1;
	delete f_in_beam2;

	return 0;
}
