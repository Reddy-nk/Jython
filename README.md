<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Java to Python Integration Example</h1>

  <p>This repository demonstrates how to integrate Java and Python using Jython. The Java portion includes a class <code>BigFunctions</code> with various methods, and the Python script <code>call_big_functions.py</code> calls these Java methods using Jython.</p>

  <h2>Java Class: <code>BigFunctions</code></h2>

  <p>The <code>BigFunctions</code> class in Java includes the following methods:</p>

  <ul>
    <li><strong><code>factorial(int n)</code></strong>: Computes the factorial of a given integer.</li>
    <li><strong><code>sortArray(int[] array)</code></strong>: Sorts an array of integers in ascending order.</li>
    <li><strong><code>filterByLength(List&lt;String&gt; list, int minLength)</code></strong>: Filters a list of strings based on their length.</li>
    <li><strong><code>concatenateStrings(String a, String b)</code></strong>: Concatenates two strings.</li>
    <li><strong><code>findMax(int[] array)</code></strong>: Finds the maximum element in an array of integers.</li>
  </ul>

  <h2>Python Script: <code>call_big_functions.py</code></h2>

  <p>The Python script <code>call_big_functions.py</code> imports the <code>BigFunctions</code> Java class using Jython and demonstrates how to call each method defined in <code>BigFunctions</code>. It showcases the interoperability between Java and Python in the context of the Jython environment.</p>

  <h2>Requirements</h2>

  <ul>
    <li>Java Development Kit (JDK)</li>
    <li>Jython</li>
    <li>Python (for running <code>call_big_functions.py</code>)</li>
  </ul>

  <h2>Usage</h2>

  <ol>
    <li><strong>Compile Java Code</strong>:
      <ul>
        <li>Compile <code>BigFunctions.java</code> into bytecode (<code>BigFunctions.class</code>).</li>
        <pre><code>javac BigFunctions.java</code></pre>
      </ul>
    </li>
    <li><strong>Run Python Script</strong>:
      <ul>
        <li>Ensure Jython is installed and configured correctly.</li>
        <li>Execute the Python script <code>call_big_functions.py</code> using Jython to see the output of calling Java methods from Python.</li>
        <pre><code>jython call_big_functions.py</code></pre>
      </ul>
    </li>
  </ol>

  <p>For a detailed introduction and installation steps, refer to the following document:</p>
  <p><a href="https://docs.google.com/document/d/1gAEFAFDE9YG4Q7EaCRiReRdbepw6x4SPZrvKQMTWzyI/edit?usp=sharing" target="_blank">Java to Python Integration Guide</a></p>

  <p>Upon running <code>call_big_functions.py</code>, you should see output similar to:</p>

  <pre>
  Factorial of 5: 120
  Sorted array: [1, 2, 3, 5, 8]
  Filtered list: ['banana', 'cherry']
  Concatenated string: Hello, world!
  Maximum element in array: 8
  </pre>

</body>
</html>
