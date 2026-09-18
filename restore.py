import sys

diff_text = """@@ -10,7 +10,6 @@
 </head>
 
 <body>
-    <canvas id="bg-canvas"></canvas>
     <div class="container">
         <div class="sidebar">
             <ul>
@@ -17,11 +17,22 @@
+                <hr>
                 <li><a href="#about" onclick="showContent('about')">About</a></li>
-                <li><a href="#research" onclick="showContent('research')">Research Projects</a></li>
-                <li><a href="#professional-service" onclick="showContent('professional-service')">Professional Service</a></li>
-                <li><a href="#teaching" onclick="showContent('teaching')">Teaching Assistantship</a></li>
+                <hr>
                 <li><a href="#education" onclick="showContent('education')">Education</a></li>
-                <li><a href="#skills" onclick="showContent('skills')">Technical Skills</a></li>
+                <hr>
+                <li><a href="#research" onclick="showContent('research')">Research Projects</a></li>
+                <hr>
                 <li><a href="#projects" onclick="showContent('projects')">Academic Projects</a></li>
+                <hr>
                 <li><a href="#courses" onclick="showContent('courses')">Courses</a></li>
+                <hr>
+                <li><a href="#skills" onclick="showContent('skills')">Technical Skills</a></li>
+                <hr>
+                <li><i class="fas fa-envelope"></i><a href="mailto:sweta@cse.iitb.ac.in"> sweta@cse.iitb.ac.in</a></li>
+                <li><i class="fab fa-linkedin"></i><a href="https://www.linkedin.com/in/sweta-8a27621a7/"> Linkedin</a>
+                </li>
+                <li><i class="fab fa-github"></i><a href="https://github.com/sweta-8"> sweta-8</a></li>
+                <!-- <li><i class="fas fa-graduation-cap"></i><a href="https://scholar.google.com/citations?user=oS7GSO0AAAAJ&hl=en&authuser=1"> sweta-8</a></li> -->
+                <hr>
             </ul>
         </div>
 
@@ -28,19 +28,19 @@
-            <div class="top-right-socials">
-                <a href="mailto:sweta@cse.iitb.ac.in" title="Email"><i class="fas fa-envelope"></i></a>
-                <a href="https://www.linkedin.com/in/sweta-8a27621a7/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
-                <a href="https://github.com/sweta-8" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
-                <a href="https://scholar.google.com/citations?user=oS7GSO0AAAAJ&hl=en&authuser=1" target="_blank" title="Google Scholar"><i class="fas fa-graduation-cap"></i></a>
-            </div>
+
             <section id="about" class="content-section">
                 <h2>Sweta 🙂</h2>
-                <div style="font-size: 1.1em; color: #60a5fa; font-weight: 500; margin-bottom: 15px; margin-top: -10px; letter-spacing: 0.5px;">Hi, Welcome to my space! 👋</div>
-                <hr>
-                <p style="text-align: justify; line-height: 1.8; color: #cbd5e1;">
-                    I am a Ph.D. scholar at IIT Bombay, working with <a href="https://www.cse.iitb.ac.in/~biswa/" target="_blank">Prof. Biswabandan Panda</a>. I am broadly interested in computing systems architecture for high performance. Specifically, I work on optimizing the <strong style="color: #60a5fa;">memory hierarchy</strong> and designing highly efficient, scalable memory subsystems for <strong style="color: #60a5fa;">many-core systems</strong>. My research interest lies in replacement policies, interconnect designs, prefetchers, hardware-software co-design, and off-chip predictors, and I have worked on Google TPUs.
-                </p>
-                <p style="color: #94a3b8; font-style: italic; font-weight: 300; margin-top: 15px;">
-                    Please feel free to reach out to me for collaborations or discussions.
-                </p>
+                <hr>
+                <p style="text-align: justify;">I am Ph.D scholar at IIT Bombay working with <a
+                        href="https://www.cse.iitb.ac.in/~biswa/">Prof. Biswabandan Panda</a> ,
+                    looking for opportunities using dynamic programming and trying to optimize search by storing my
+                    errors in a table, performing push
+                    operations in my skills stack using a linked list to avoid stack overflow. Currently, my cache is
+                    mostly occupied with
+                    computer architecture concepts as I am trying to explore various microarchitecture components.
+                    I have recently initialized my instruction pointer to the last level caches. With a robust
+                    foundation in fundamental computer science concepts, including algorithms, data structures, computer
+                    organization, compiler
+                    design and operating systems. I am constantly striving to expand my knowledge and skills in computer
+                    science.</p>
                 <!-- <button class="next-tab" onclick="nextTab('education')">Next &darr;</button> -->
                 <hr>
 
@@ -47,157 +47,69 @@
 
-                <div class="google-card-anim" style="display: flex; align-items: flex-start; gap: 20px; margin-bottom: 20px; background: rgba(30, 41, 59, 0.4); padding: 20px; border-radius: 12px; border: 1px solid #1e293b;">
-                    <div style="flex-shrink: 0; border-radius: 12px; overflow: hidden; width: 120px; height: 120px; box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
-                        <img src="images/google_tpu_square.png" alt="Google TPU Accelerator" style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
-                    </div>
-                    <div style="flex-grow: 1;">
-                        <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap;">
-                            <strong style="font-size: 1.15em; color: #f8fafc;">Silicon Engineering Intern</strong>
-                            <span style="color: #94a3b8; font-size: 0.95em;">May 2026 – July 2026</span>
-                        </div>
-                        <div style="color: #cbd5e1; margin-top: 4px; font-size: 0.95em;">
-                            <a href="https://about.google/" target="_blank" class="google-text-anim" style="text-decoration: none;">Google</a>, Bengaluru, India
-                        </div>
-                        <div style="margin-top: 12px; color: #cbd5e1; line-height: 1.6;">
-                            Worked with the Google hardware team to architect and optimize the interconnect design for Next-Generation <a href="https://cloud.google.com/tpu" target="_blank" style="color: #60a5fa; text-decoration: none;">Tensor Processing Units (TPUs)</a>.
-                        </div>
-                    </div>
-                </div>
-                <hr>
-
-                <h2>News:</h2>
-                <ul class="timeline">
-                    <li>
-                        <span class="timeline-date">Feb 2026</span>
-                        <div class="timeline-content">Drishti, recognized among distinguished Posters at ACM India ARCS 2026</div>
-                    </li>
-                    <li>
-                        <span class="timeline-date">Oct 2025</span>
-                        <div class="timeline-content">Drishti, nominated as one of the best paper candidates at MICRO 2025.</div>
-                    </li>
-                    <li>
-                        <span class="timeline-date">Sep 2025</span>
-                        <div class="timeline-content">Received the Winifred B. Fernandes Award for excellence in PhD research progress.🙏</div>
-                    </li>
-                    <li>
-                        <span class="timeline-date">July 2025</span>
-                        <div class="timeline-content">🥳 My first work <i>"Drishti: Do Not Forget Slicing While Designing Last-Level Cache Replacement Policies for Many-Core Systems" </i>has been accepted at the 58th IEEE/ACM International Symposium on Microarchitecture <a href="https://microarch.org/micro58/">(MICRO'25)</a></div>
-                    </li>
-                    <li>
-                        <span class="timeline-date">April 2025</span>
-                        <div class="timeline-content">Submitted my first work at 58th IEEE/ACM International Symposium on Microarchitecture <a href="https://microarch.org/micro58/">(MICRO'25)</a></div>
-                    </li>
-                </ul>
-            </section>
-
-            <section id="professional-service" class="content-section" style="display:none;">
+                <p>
+                    <strong>Silicon Engineering Intern</strong>,
+                    <a href="https://about.google/" target="_blank">Google</a>,
+                    Bengaluru, India
+                    <span style="float:right;"><em>May 2026 – July 2026</em></span>
+                </p>
+                <hr>
+
                 <h2>Professional Service</h2>
-                <ul class="timeline" style="margin-top: 30px;">
-                    <li>
-                        <div class="timeline-date">2026 - Present</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa; display: flex; align-items: center; gap: 8px;">
-                                <i class="fas fa-book-open" style="font-size: 1.2em; color: #94a3b8;"></i>
-                                Reviewer
-                            </strong>
-                            <div style="color: #cbd5e1; margin-top: 5px;">IEEE Computer Architecture Letters (<strong>CAL</strong>)</div>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">2026</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa; display: flex; align-items: center; gap: 8px;">
-                                <img src="images/micro_logo.png" alt="MICRO" style="height: 1.2em; background-color: rgba(255,255,255,0.8); border-radius: 4px; padding: 2px;">
-                                Student Reviewer
-                            </strong>
-                            <div style="color: #cbd5e1; margin-top: 5px;">ACM/IEEE International Symposium on Microarchitecture (<strong>MICRO 2026</strong>)</div>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">2026</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa; display: flex; align-items: center; gap: 8px;">
-                                <img src="images/isca.png" alt="ISCA" style="height: 1.2em; background-color: rgba(255,255,255,0.8); border-radius: 4px; padding: 2px;">
-                                Artifact Evaluation Committee
-                            </strong>
-                            <div style="color: #cbd5e1; margin-top: 5px;">ACM/IEEE International Symposium on Computer Architecture (<strong>ISCA 2026</strong>)</div>
-                        </div>
-                    </li>
-                </ul>
-            </section>
-
-            <section id="teaching" class="content-section" style="display:none;">
-                <h2>Teaching Assistantship</h2>
-                <p style="color: #94a3b8; font-style: italic; margin-bottom: 25px;">Computer Science and Engineering, IIT Bombay</p>
-                <ul class="timeline">
-                    <li>
-                        <div class="timeline-date">July 2026 - Present</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa;">CS230: Digital Logic Design + Computer Architecture</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Sayandeep Saha</em></span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">Jan 2026 - Apr 2026</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa;">CS794: Systems for Machine Learning</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Mythili Vutukuru</em></span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">Jun 2025 - Dec 2025</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa;">CS231: Digital Logic + Computer Architecture Lab</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Biswabandan Panda</em></span>
-                            
-                            <hr style="border: 0; height: 1px; background: #334155; margin: 12px 0;">
-                            
-                            <strong style="color: #60a5fa;">CS230: Digital Logic Design + Computer Architecture</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Sayandeep Saha</em></span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">Jan 2025 - Jun 2025</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa;">CS899: Communication Skills</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Varsha Apte</em></span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">Aug 2024 - Dec 2024</div>
-                        <div class="timeline-content">
-                            <strong style="color: #60a5fa;">CS101: Computer Programming and Utilization</strong><br>
-                            <span style="color: #cbd5e1;"><em>Prof. Manoj Prabhakaran</em></span>
-                        </div>
-                    </li>
-                </ul>
-            </section>
-
+
+                <strong>Student Reviewer</strong>: ACM/IEEE International Symposium on Microarchitecture (<strong>MICRO
+                    2026</strong>) <br>
+                <strong>Artifact Evaluation Committee</strong>: ACM/IEEE International Symposium on Computer
+                Architecture (<strong>ISCA 2026</strong>)
+
+
+                <hr>
+                <h2>News:</h2>
+                <ul>
+                    <li>[Feb'26] Drishti, recognized among distinguished Posters at ACM India ARCS 2026</li>
+                    <hr>
+                    <li>[Oct'25] Drishti, nominated as one of the best paper candidates at MICRO 2025.</li>
+                    <hr>
+                    <li>[Sep'25] Received the Winifred B. Fernandes Award for excellence in PhD research progress.🙏
+                    </li>
+                    <hr>
+                    <li>[July'25] 🥳 My first work <i>"Drishti: Do Not Forget Slicing While Designing Last-Level Cache
+                            Replacement Policies for Many-Core Systems" </i>has been accepted at the 58th IEEE/ACM
+                        International Symposium on Microarchitecture <a
+                            href="https://microarch.org/micro58/">(MICRO'25)</a></li>
+                    <hr>
+                    <li>[April'25] Submitted my first work at 58th IEEE/ACM International Symposium on Microarchitecture
+                        <a href="https://microarch.org/micro58/">(MICRO'25)</a></li>
+                    <hr>
+                </ul>
+            </section>
             <section id="education" class="content-section" style="display:none;">
                 <h2>Education</h2>
-                <ul class="timeline">
-                    <li>
-                        <div class="timeline-date">Jan. 2024 - Present</div>
-                        <div class="timeline-content">
-                            <a href="https://www.iitb.ac.in/" target="_blank" style="color: #60a5fa; text-decoration: none;"><strong>Indian Institute of Technology, Bombay</strong></a><br>
-                            Ph.D., Computer Science and Engineering<br>
-                            <span style="color: #94a3b8; font-size: 0.95em;">CGPA: 8.17</span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">July 2023 - Jan. 2024</div>
-                        <div class="timeline-content">
-                            <a href="https://www.iith.ac.in/" target="_blank" style="color: #60a5fa; text-decoration: none;"><strong>Indian Institute of Technology, Hyderabad</strong></a><br>
-                            Ph.D., Computer Science and Engineering<br>
-                            <span style="color: #94a3b8; font-size: 0.95em;">Switched to IITB</span>
-                        </div>
-                    </li>
-                    <li>
-                        <div class="timeline-date">Aug. 2019 - Aug. 2023</div>
-                        <div class="timeline-content">
-                            <a href="https://beu-bih.ac.in/" target="_blank" style="color: #60a5fa; text-decoration: none;"><strong>Bihar Engineering University, Patna</strong></a><br>
-                            Bachelor of Technology in Computer Science and Engineering<br>
-                            <span style="color: #94a3b8; font-size: 0.95em;">CGPA: 8.32</span>
-                        </div>
+                <hr>
+                <ul>
+                    <li>
+                        <a href="https://www.iitb.ac.in/"><strong>Indian Institute of Technology, Bombay</strong></a>
+                        (Jan. 2024)<br>
+                        <i>Ph.D, Computer Science and Engineering<br>
+                            CGPA: 8.17</i>
+                    </li>
+                    <hr>
+                    <li>
+                        <a href="https://www.iith.ac.in/"><strong>Indian Institute of Technology, Hyderabad</strong></a>
+                        (July 2023)<br>
+                        <i>Ph.D, Computer Science and Engineering<br>
+                            Switched to IITB</i>
+                    </li>
+                    <hr>
+                    <li>
+                        <a href="https://beu-bih.ac.in/"><strong>Bihar Engineering University, Patna</strong></a> (Aug.
+                        2019 - Aug. 2023)<br>
+                        <i>Bachelor of Technology in Computer Science and Engineering<br>
+                            CGPA: 8.32</i>
+                    </li>
+                    <hr>
+                    <li>
+                        <strong>Jesus & Mary Academy, Darbhanga</strong> (May 2016 - May 2018)<br>
+                        <i>Senior Secondary (CBSE, Class XII)<br>
+                            Percentage: 78.4%</i>
                     </li>
                 </ul>
             </section>
@@ -204,16 +204,17 @@
             <!-- Courses------------------------------------------------------------------------- -->
             <section id="courses" class="content-section" style="display:none;">
                 <h2>Courses</h2>
-                <div style="color: #94a3b8; font-style: italic; margin-bottom: 20px;">Indian Institute of Technology, Bombay</div>
-                <ul class="course-grid">
-                    <li class="course-card"><div class="course-code">CS219</div><div class="course-name">Operating Systems</div></li>
-                    <li class="course-card"><div class="course-code">CS684</div><div class="course-name">Embedded Systems</div></li>
-                    <li class="course-card"><div class="course-code">CS695</div><div class="course-name">Topics in Virtualization and Cloud Computing</div></li>
-                    <li class="course-card"><div class="course-code">CS683</div><div class="course-name">Advanced Computer Architecture</div></li>
-                    <li class="course-card"><div class="course-code">CS771</div><div class="course-name">Foundations of Verification and Automated Reasoning</div></li>
-                    <li class="course-card"><div class="course-code">CS773</div><div class="course-name">Computer Architecture for Performance and Security</div></li>
-                    <li class="course-card"><div class="course-code">CS614</div><div class="course-name">Advanced Compilers</div></li>
-                    <li class="course-card"><div class="course-code">CSS801</div><div class="course-name">Seminar</div></li>
+                <hr>
+                <!-- <p>..</p> -->
+                <ul>
+                    <li>CS219: Operating Systems</li>
+                    <li>CS684: Embedded Systems</li>
+                    <li>CS695: Topics in Virtualization and Cloud Computing</li>
+                    <li>CS683: Advanced Computer Architecture</li>
+                    <li>CS771: Foundations of verification and automated reasoning</li>
+                    <li>CS773: Computer Architecture for Performance and Security</li>
+                    <li>CS614: Advanced Compilers</li>
+                    <li>CSS801:Seminar</li>
                 </ul>
             </section>
 
@@ -220,19 +220,9 @@
             <!-- Skills------------------------------------------------------------------------- -->
             <section id="skills" class="content-section" style="display:none;">
-                <h2>Technical Skills</h2>
-                <ul style="display: flex; flex-direction: column; gap: 20px; list-style: none; padding: 0;">
-                    <li class="course-card" style="width: 100%; box-sizing: border-box;">
-                        <div class="course-code" style="margin-bottom: 10px; font-size: 1.1em;"><i class="fas fa-code" style="color: #60a5fa; margin-right: 8px;"></i>Languages</div>
-                        <div style="color: #cbd5e1; font-size: 0.95em; line-height: 1.6;">C, C++, JAVA, Python, Heptagon, HTML/CSS</div>
-                    </li>
-                    <li class="course-card" style="width: 100%; box-sizing: border-box;">
-                        <div class="course-code" style="margin-bottom: 10px; font-size: 1.1em;"><i class="fas fa-microchip" style="color: #60a5fa; margin-right: 8px;"></i>Simulators</div>
-                        <div style="color: #cbd5e1; font-size: 0.95em; line-height: 1.6;">gem5, ChampSim, PCACTI, McPAT, HotSpot</div>
-                    </li>
-                    <li class="course-card" style="width: 100%; box-sizing: border-box;">
-                        <div class="course-code" style="margin-bottom: 10px; font-size: 1.1em;"><i class="fas fa-tools" style="color: #60a5fa; margin-right: 8px;"></i>Developer Tools</div>
-                        <div style="color: #cbd5e1; font-size: 0.95em; line-height: 1.6;">Git, Docker, VS Code</div>
-                    </li>
+                <hr>
+                <ul>
+                    <li><b>Languages:</b> C, C++, Python, Heptagon</li>
+                    <li><b>Simulator:</b> Champsim, PCACTI, McPAT, HotSpot</li>
                 </ul>
             </section>
 
@@ -239,36 +239,16 @@
             <section id="research" class="content-section" style="display:none;">
                 <h2>Research Projects</h2>
                 <hr>
-                <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid #1e293b; border-radius: 12px; padding: 25px; margin-bottom: 25px; transition: transform 0.3s ease, background 0.3s ease;" onmouseover="this.style.background='rgba(30, 41, 59, 0.7)'; this.style.transform='translateY(-3px)';" onmouseout="this.style.background='rgba(30, 41, 59, 0.4)'; this.style.transform='translateY(0)';">
-                    <div style="color: #f43f5e; font-weight: bold; font-size: 0.9em; margin-bottom: 8px; letter-spacing: 0.5px; display: flex; align-items: center; gap: 5px;">
-                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
-                        BEST PAPER CANDIDATE AT MICRO '25
-                    </div>
-                    <h3 style="margin-top: 0; color: #60a5fa; display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap;">
-                        <span><a href="https://dl.acm.org/doi/pdf/10.1145/3725843.3756028?__cf_chl_tk=vPw.nHyQYh4LdP_c5ZTSPae7b2pJqDHBfodDxBg25cM-1789727736-1.0.1.1-djgBnjx60moDGhR.D1YZwqXN6OVLBM0iiym7DeysBUs" target="_blank" style="color: #60a5fa; text-decoration: none;">Drishti: Do Not Forget Slicing While Designing Last-Level Cache Replacement Policies for Many-Core Systems</a></span>
-                        <span style="font-size: 0.85em; color: #94a3b8; font-weight: normal;">MICRO 2025</span>
-                    </h3>
-                    <p style="color: #94a3b8; margin-bottom: 20px; font-size: 0.95em;"><em>Co-authored with Prerna Priyadarshini and Prof. Biswabandan Panda</em></p>
-                    <p style="color: #e2e8f0; line-height: 1.8; text-align: justify; margin-bottom: 20px;">
-                        Modern many-core systems organize the Last-Level Cache (LLC) into multiple slices, yet state-of-the-art replacement policies often treat the LLC as a monolithic entity. This oversight leads to localized learning inaccuracies and biased sample sets when applied to distributed cache slices. In this work, we propose <strong>Drishti</strong>, a novel cache management logic that explicitly incorporates slicing to effectively handle the distributed nature of the LLC. By introducing a per-core global reuse predictor combined with a local (per-slice) sampled cache, Drishti overcomes the limitations of centralized sample sets and significantly improves overall cache performance.
-                    </p>
-                    <a href="https://dl.acm.org/doi/pdf/10.1145/3725843.3756028?__cf_chl_tk=vPw.nHyQYh4LdP_c5ZTSPae7b2pJqDHBfodDxBg25cM-1789727736-1.0.1.1-djgBnjx60moDGhR.D1YZwqXN6OVLBM0iiym7DeysBUs" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; background: rgba(96, 165, 250, 0.1); border: 1px solid #60a5fa; color: #60a5fa; border-radius: 6px; text-decoration: none; font-size: 0.9em; font-weight: bold; transition: background 0.3s ease;" onmouseover="this.style.background='rgba(96, 165, 250, 0.2)';" onmouseout="this.style.background='rgba(96, 165, 250, 0.1)';">
-                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
-                        Read Paper
-                    </a>
-                </div>
-
-                <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid #1e293b; border-radius: 12px; padding: 25px; transition: transform 0.3s ease, background 0.3s ease;" onmouseover="this.style.background='rgba(30, 41, 59, 0.7)'; this.style.transform='translateY(-3px)';" onmouseout="this.style.background='rgba(30, 41, 59, 0.4)'; this.style.transform='translateY(0)';">
-                    <h3 style="margin-top: 0; color: #60a5fa; display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap;">
-                        <span>Design & Implementation of Sliced LLC</span>
-                        <span style="font-size: 0.85em; color: #94a3b8; font-weight: normal;">Jan 2024 - April 2024</span>
-                    </h3>
-                    <p style="color: #94a3b8; margin-bottom: 20px; font-size: 0.95em;"><em>Guide: <a href="https://www.cse.iitb.ac.in/~biswa/" target="_blank" style="color: #cbd5e1; text-decoration: underline;">Prof. Biswabandan Panda</a>, IIT Bombay</em></p>
-                    <ul style="color: #e2e8f0; line-height: 1.7; padding-left: 20px;">
-                        <li style="margin-bottom: 10px;">Implemented sliced LLC in Champsim simulator by connecting all slices using ring interconnection network.</li>
-                        <li>Added queues to avoid duplicate packets that have writeback or load requests to the same address in the ring network.</li>
-                    </ul>
-                </div>
+                <h3>Design & Implementation of Sliced LLC<span style="float:right;">(Jan 2024 - April 2024)</span> </h3>
+                <p><em>Guide: <a href="https://www.cse.iitb.ac.in/~biswa/" target="_blank">Prof. Biswabandan Panda</a>,
+                        Computer Science and Engineering, IIT Bombay</em></p>
+
+                <ul>
+                    <li>Implemented sliced LLC in Champsim simulator by connecting all slices using ring interconnection
+                        network</li>
+                    <li>Added queues to avoid duplicate packets that have writeback or load requests to the same address
+                        in the ring network.</li>
+                </ul>
 
             </section>
 
"""

import sys

def apply_reverse_patch(file_path, diff_content):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    diff_lines = diff_content.splitlines()
    
    # Very rudimentary patch applier focusing purely on finding the exact chunks.
    # Since I know the full diff and file, I can parse chunks and apply them backward.
    # But it's easier to just save the old state from the log if available.
    
    # Because applying unified diff manually is error-prone, let's format it as a valid patch and use `patch -R`.
    
    patch_str = f"--- index.html\\n+++ index.html\\n"
    for line in diff_lines:
        if line.startswith("@@"):
            patch_str += line + "\\n"
        elif line.startswith("-") or line.startswith("+") or line.startswith(" "):
            patch_str += line + "\\n"
        else:
            patch_str += " " + line + "\\n" # Fallback context
            
    with open("reverse.patch", "w") as pf:
        pf.write(patch_str)

apply_reverse_patch("index.html", diff_text)
