<h1>IBM Translational Model-1</h1>

<p><b>Language:</b>	Python 3.5</p>

<h2>Aim:</h2>
To implement the IBM Model-1 which finds the lexical translation of the words in the corpus by using the EM (Expectation Maximization) algorithm.

<h2>Working:</h2>

1.	The data is present in data1.json, which consists of 5 Franch sentences and the corresponding English translation of each sentence. The data is present as a dictionary.
2.	Using the data in the dictionary, all the unique French and English words were extracted into 2 lists.
3.	The EM algorithm is run till convergence is achieved (usually by 10-20 iterations).
4.	The alignment of the sentences is then printed after EM algorithm completes.
5. 	To run the code, simply run model1.py.

<h2>Installation:</h2>

To run the following code, Anaconda needs to be readily installed.
<li>Anaconda can be installed by following the following link: https://docs.anaconda.com/anaconda/install/</li>
