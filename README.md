<p>This tool takes each subnet in subnet1 list and checks if it is in the subnet2 list or subnet in subnet2 list is within the subnet1 list, if subnet1 subnet is not matching any of this check, it will be written to a file&nbsp;<br />
subnet1.csv and subnet2.csv should be <strong>sorted as integer ascending as below examples</strong>, it is done by sortout function in the code&nbsp;<br />
<strong>subnet1.csv</strong>&nbsp;<br />
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="1.2.0.0/24,1234,12<br />
1.12.0.0/23,3456,34<br />
1.34.44.0/24,566,45<br />
2.12.45.0/25,345,8<br />"><pre class="notranslate"><code>1.2.0.0/24,1234,12<br />
1.12.0.0/23,3456,34<br />
1.34.44.0/24,566,45<br />
2.12.45.0/25,345,8<br />
</code></pre></div>
 <strong>subnet2.csv</strong><br />
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="1.1.0.0/23,8769,1<br />
1.2.0.0/25,555,54<br />
1.34.44.0/23,234,52<br />
2.12.45.0/25,490,27<br />"><pre class="notranslate"><code>1.1.0.0/23,8769,1<br />
1.2.0.0/25,555,54<br />
1.34.44.0/23,234,52<br />
2.12.45.0/25,490,27<br />
</code></pre></div>
as seen below between the start and end date 1.12.0.0/23 is not within any subnet and no subnet on subnet2.csv is within 1.12.0.0/23.<br />
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="1.2.0.0/24&lt;-1.2.0.0/25&nbsp; &nbsp;<br />
1.34.44.0/24-&gt;1.34.44.0/23<br />
2.12.45.0/25-&gt;2.12.45.0/25<br />"><pre class="notranslate"><code>1.2.0.0/24&lt;-1.2.0.0/25&nbsp; &nbsp;<br />
1.34.44.0/24-&gt;1.34.44.0/23<br />
2.12.45.0/25-&gt;2.12.45.0/25<br />
</code></pre></div>
#RESULT#&nbsp;<br />
<strong>subnetnotmatch.txt</strong><br />
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="2023-03-18 22:34:12.348187<br />
1.12.0.0/23<br />
2023-03-18 22:34:12.427192<br />"><pre class="notranslate"><code>2023-03-18 22:34:12.348187<br />
1.12.0.0/23,3456,34<br />
2023-03-18 22:34:12.427192<br />
</code></pre></div>
</p>



