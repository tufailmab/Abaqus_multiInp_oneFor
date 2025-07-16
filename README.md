</head>
<body>
  <h1>Abaqus_multiInp_oneFor</h1>

  <p>This project provides a Python script to automate the batch submission of Abaqus jobs using <strong>multiple <code>.inp</code> files</strong> with a <strong>single <code>.for</code> user subroutine</strong>. It is ideal for scenarios where you want to test or simulate different models using the same custom material behavior or user logic implemented in Fortran.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Batch Execution:</strong> Automatically creates and submits Abaqus jobs for each <code>.inp</code> file found in the current directory.</li>
    <li><strong>Single Subroutine:</strong> Uses one <code>.for</code> file as the user subroutine for all simulations.</li>
    <li><strong>Clean Job Naming:</strong> Automatically generates safe job names for each combination of input and subroutine.</li>
    <li><strong>Execution Monitoring:</strong> Waits for each job to complete before moving on to the next.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Place all your <code>.inp</code> files and a single <code>.for</code> file in the same folder as the script.</li>
    <li>Run the script from within that directory using Abaqus Python:
      <pre><code>abaqus python WithSubroutine.py</code></pre>
    </li>
    <li>The script will:
      <ul>
        <li>Validate the presence of exactly one <code>.for</code> file</li>
        <li>Create a job for each <code>.inp</code> file using that subroutine</li>
        <li>Submit the jobs and wait for completion</li>
      </ul>
    </li>
  </ol>

  <h2>Requirements</h2>
  <ul>
    <li>Abaqus with Python scripting enabled</li>
    <li>One valid <code>.for</code> file</li>
    <li>Multiple valid <code>.inp</code> files</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>. You are free to use, modify, and distribute this tool as you like. Please give credit if you build upon it.</p>

  <h2>Developer Info</h2>
  <ul>
    <li><strong>Developer:</strong> Your Name</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> Contributions and improvements are welcome!</li>
  </ul>
</body>
