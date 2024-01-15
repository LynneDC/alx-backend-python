<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">
    <h1 class="gap">0x01. Python - Async</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:19,&quot;value&quot;:&quot;Python&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:35,&quot;value&quot;:&quot;Back-end&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;author&quot;:&quot;Emmanuel Turlay, Staff Software Engineer at Cruise&quot;,&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:false,&quot;auto_correction_available_at&quot;:&quot;2024-01-15T12:00:00.000+02:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-01-15T06:00:00.000+02:00&quot;,&quot;ends_at&quot;:&quot;2024-01-16T06:00:00.000+02:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-01-20T06:00:00.000+02:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"></div>
    
  <div class="panel-body">
    <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/4aeaa9c3cb1f316c05c4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240115T075804Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fc6d8762db8b75ab76789458ed70d39b82fe1f7b75e9e46594dc7110d1f836cc" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/zYkXScziW1D5rNdNEvObjQ" title="Async IO in Python: A Complete Walkthrough" target="_blank">Async IO in Python: A Complete Walkthrough</a></li>
<li><a href="/rltoken/aZUO4GiWHbPIrVBIwptFAw" title="asyncio - Asynchronous I/O" target="_blank">asyncio - Asynchronous I/O</a></li>
<li><a href="/rltoken/72mVf1s8rx2ih_U2WjBmaA" title="random.uniform" target="_blank">random.uniform</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/RzzuxS2J7-SysSxP0Hu3cA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li><code>async</code> and <code>await</code> syntax</li>
<li>How to execute an async program with <code>asyncio</code></li>
<li>How to run concurrent coroutines</li>
<li>How to create <code>asyncio</code> tasks</li>
<li>How to use the <code>random</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.x)</li>
<li>All your functions and coroutines must be type-annotated.</li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

  </div>
</div>
    <h2 class="gap">Tasks</h2>
        <div data-role="task11625" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11625">
  <span id="user_id" data-id="251885"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. The basics of async
    </h3>
        <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="251885"></span>
    <!-- Progress vs Score -->
     <!-- Task Body -->
    <p>Write an asynchronous coroutine that takes in an integer argument (<code>max_delay</code>, with a default value of 10) named <code>wait_random</code> that waits for a random delay between 0 and <code>max_delay</code> (included and float value) seconds and eventually returns it.</p>

<p>Use the <code>random</code> module.</p>
      </div>
    <div data-role="task11626" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-11626">
  <span id="user_id" data-id="251885"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Let&#39;s execute multiple coroutines at the same time with async
    </h3>
    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="251885"></span>
    <!-- Progress vs Score -->
    <!-- Task Body -->
    <p>Import <code>wait_random</code> from the previous python file that you&rsquo;ve written and write an async routine called <code>wait_n</code> that takes in 2 int arguments (in this order): <code>n</code> and <code>max_delay</code>. You will spawn <code>wait_random</code> <code>n</code> times with the specified <code>max_delay</code>.</p>

<p><code>wait_n</code> should return the list of all the delays (float values). The list of the delays should be in ascending order without using <code>sort()</code> because of concurrency.</p>


