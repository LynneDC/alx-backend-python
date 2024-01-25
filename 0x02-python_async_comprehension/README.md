<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body> 
       <h1 class="gap">0x02. Python - Async Comprehension</h1>
      <div id="project_id" style="display: none" data-project-id="1231"></div>
      <div class="panel-body">
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240125T171647Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bb4226acf12148165db5ce5be0386548518d441090e7fd158755691d29dd8268" alt="" loading='lazy' style="" /></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
    <ul>
<li><a href="/rltoken/hlwtED-iLsdORSgly8DsyQ" title="PEP 530 -- Asynchronous Comprehensions" target="_blank">PEP 530 &ndash; Asynchronous Comprehensions</a></li>
<li><a href="/rltoken/0OkbObYzCKtO7ZUAxfKvkw" title="What’s New in Python: Asynchronous Comprehensions / Generators" target="_blank">What’s New in Python: Asynchronous Comprehensions / Generators</a></li>
<li><a href="/rltoken/l4Fnno568VbVIn9GvrFVtQ" title="Type-hints for generators" target="_blank">Type-hints for generators</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>KNOWLEDGE CHECK</p>

<ul>
<li>How to write an asynchronous generator</li>
<li>How to use async comprehensions</li>
<li>How to type-annotate generators</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
    <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
    <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
    <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the <code>pycodestyle</code> style (version 2.5.x)</li>
    <li>The length of your files will be tested using <code>wc</code></li>
    <li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
    <li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
    <li>All your functions and coroutines must be type-annotated.</li>
</ul>
<h2 class="gap">TASKS</h2>
     <div data-role="task11630" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11630">
        <span id="user_id" data-id="251885"></span>
    </div>
    </div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Async Generator
    </h3>
    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
  </div>
  </div>
  <p>Write a coroutine called <code>async_generator</code> that takes no arguments. </p>
<p>The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the <code>asyncio.sleep</code> function to do this.</p>
        <div class="modal-body">
        
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Async Comprehensions
    </h3>
     <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
  <p>Import <code>async_generator</code> from the previous task and then write a coroutine called <code>async_comprehension</code> that takes no arguments. </p>

<p>The coroutine will collect 10 random numbers using an async comprehensing over <code>async_generator</code>, then return the 10 random numbers.</p>
<h3 class="panel-title">
    2. Run time for four parallel comprehensions
</h3>
   <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>
    <!-- Task Body -->
    <p>Import <code>async_comprehension</code> from the previous file and write a <code>measure_runtime</code> coroutine that will execute <code>async_comprehension</code> four times in parallel using <code>asyncio.gather</code>.</p>

<p><code>measure_runtime</code> should measure the total runtime and return it.</p>

<p>Notice that the total runtime is roughly 10 seconds, explain it to yourself.</p>
</body>
</html>