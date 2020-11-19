# funds-explorer-filter

 Real State Funds Explorer Filter

## Comments to v1 - stable version

Information captured and processed in pandas dataframe from fundsexplorer.com.br/ranking [click](https://www.fundsexplorer.com.br/ranking).
Historical prices captured in Yahoo Finance using pandas data-reader.
Cost price calculated as last 200 days average minus 1 standard deviation. In case of NaN, estimated in 80% of current price.

Graphs generated in main as follows:
-My Funds - 12, 24 and 36 months forward;
-Brick Funds - 12, 24 and 36 months forward;
-Paper Funds - 12 months forward.

Graphs generated in Jupyter as follows:
1-My Funds - 12 months forward;
2-Brick Funds - 12 months forward;
3-Paper Funds - 12 months forward.

Change to the desired assets (shares) you want in my_rsf
Change the "to_excel" codes of my_rsf, rsf_brick and rsf_paper to your own computer desired path

Using Jupyter in Google Colab:
1- Include in code the 2 snippets commented at the beginning adjusting to your path in Google;
2-Comment the "to_excel" and "os.rename" snippets of code as you do want (or can not) to save data in excel file and rename the graph file tmp-plot.html in Google Colab environment.
ATENTION: RENDERING GRAPHICS ARE FAILING IN GOOGLE COLAB!
