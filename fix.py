import sys

with open('c:/Users/ok/OneDrive/Infabio/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("            display: flex;\n            justify-content: center;\n", "")
css = css.replace("            width: 1440px;\n", "            width: 100%;\n            max-width: 1440px;\n            margin: 0 auto;\n            overflow-x: hidden;\n")
# fallback for crlf
css = css.replace("            display: flex;\r\n            justify-content: center;\r\n", "")
css = css.replace("            width: 1440px;\r\n", "            width: 100%;\r\n            max-width: 1440px;\r\n            margin: 0 auto;\r\n            overflow-x: hidden;\r\n")

css = css.replace("            display: flex;\n            justify-content: center;", "")
css = css.replace("            width: 1440px;", "            width: 100%;\n            max-width: 1440px;\n            margin: 0 auto;\n            overflow-x: hidden;")
css = css.replace("            display: flex;\r\n            justify-content: center;", "")
css = css.replace("            width: 1440px;", "            width: 100%;\r\n            max-width: 1440px;\r\n            margin: 0 auto;\r\n            overflow-x: hidden;")

with open('c:/Users/ok/OneDrive/Infabio/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('c:/Users/ok/OneDrive/Infabio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = "<!-- Image 1 & 4 & 6: From Defense to Domination (Case Studies) -->"
end = "        <!-- Image 2: Why Clients Trust Us -->"

s_idx = html.find(start)
e_idx = html.find(end)

replacement = """<!-- Image 1 & 4 & 6: From Defense to Domination (Case Studies) -->
        <section style="background: var(--bg-off-white); position: relative;">
            <div class="section-label">DEFENSE TO DOMINATION CASE STUDIES (Img 1, 4, 6)</div>
            
            <div style="text-align: center; margin-bottom: 20px;">
                <div class="badge" style="background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;">
                   [ Green Check ] Indian Business Victory Stories
                </div>
            </div>
            <div class="section-header-centered">
                <h2 class="section-title" style="font-size: 56px;">From Defense to Domination</h2>
                <p class="section-subtitle">Real businesses, real threats neutralized, real market victories across diverse sectors.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 60px;">
                
                <!-- Card-Style 1: E-commerce Fashion (Mumbai) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">E-commerce Fashion</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Mumbai</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Cart abandonment rate of 78%, bleeding ₹2.3L daily in wasted ad spend</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">AI-powered retargeting + email recovery sequences + conversion optimization</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px; margin-bottom: 20px;">Revenue up 3.4x, cart abandonment down to 18% in 60 days</p>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

                <!-- Card-Style 2: SaaS B2B (Bengaluru) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">SaaS B2B</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Bengaluru</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Lead cost at ₹8,400 per qualified lead, burning through budget</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">LinkedIn precision targeting + content defense strategy + lead scoring AI</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px; margin-bottom: 20px;">Lead volume doubled, CPA reduced by 74%</p>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

                <!-- Card-Style 3: Healthcare Clinic (Delhi) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">Healthcare Clinic</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Delhi</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Zero online visibility, competitor dominating local search</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Local SEO warfare + reputation shield + Google Ads precision strike</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px; margin-bottom: 20px;">#1 Rank on Maps, 4x more inbound patient inquiries</p>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

                <!-- Case Study 4 (Original EdTech) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">EdTech Platform</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Pune</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Student acquisition cost of ₹3,200, unsustainable growth</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Social media warfare + influencer network + conversion funnel optimization</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 10px;">
                                        <div>
                                            <div style="color: #94a3b8; font-size: 12px;">Before</div>
                                            <div style="font-weight: 800;">250 students/m</div>
                                        </div>
                                        <div style="text-align: right;">
                                            <div style="color: var(--accent-green); font-size: 12px;">After</div>
                                            <div style="font-weight: 800; color: #22c55e;">1,840 students/m</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

                <!-- Case Study 5 (Original Manufacturing) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 1px solid #e2e8f0; height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">Manufacturing Export</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Ahmedabad</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Struggling to reach international buyers, sales stagnant</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Global expansion strategy + B2B outreach + trade show digital amplification</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 10px;">
                                        <div>
                                            <div style="color: #94a3b8; font-size: 12px;">Before</div>
                                            <div style="font-weight: 800;">$180K/year</div>
                                        </div>
                                        <div style="text-align: right;">
                                            <div style="color: var(--accent-green); font-size: 12px;">After</div>
                                            <div style="font-weight: 800; color: #22c55e;">$1.1M/year</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

                <!-- Case Study 6 (Original Real Estate Highlighted) -->
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="background: white; border-radius: 20px; padding: 40px; border: 3px solid var(--accent-blue); height: 100%;">
                                <div style="margin-bottom: 30px;">
                                    <h4 style="color: var(--accent-blue); font-weight: 800; margin-bottom: 4px;">Real Estate Developer</h4>
                                    <span style="color: #94a3b8; font-size: 14px;">Gurugram</span>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-red);">[ ! ]</span>
                                        <strong style="font-weight: 700;">Threat Detected</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Property launch budget wasted on wrong audiences, poor ROI</p>
                                </div>
                                <div style="margin-bottom: 24px;">
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-blue);">[ Guard ]</span>
                                        <strong style="font-weight: 700;">Defense Deployed</strong>
                                    </div>
                                    <p style="color: #64748b; font-size: 15px;">Data-driven buyer persona targeting + premium property marketing + VR integration</p>
                                </div>
                                <div>
                                    <div style="display: flex; gap: 12px; margin-bottom: 12px;">
                                        <span style="color: var(--accent-orange);">[ Cup ]</span>
                                        <strong style="font-weight: 700;">Market Domination Achieved</strong>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 10px;">
                                        <div>
                                            <div style="color: #94a3b8; font-size: 12px;">Before</div>
                                            <div style="font-weight: 800;">4 units/m</div>
                                        </div>
                                        <div style="text-align: right;">
                                            <div style="color: var(--accent-green); font-size: 12px;">After</div>
                                            <div style="font-weight: 800; color: #22c55e;">22 units/m</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div style="width: 64px; height: 64px; background: var(--accent-blue, #3b82f6); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                            </div>
                            <h4 style="font-weight: 800; color: white; font-size: 20px;">Watch Video</h4>
                            <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Case Study Breakdown</p>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

if s_idx != -1 and e_idx != -1:
    new_html = html[:s_idx] + replacement + "\n" + html[e_idx:]
    with open('c:/Users/ok/OneDrive/Infabio/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML fixed successfully")
else:
    print(f"Indices not found. s_idx: {s_idx}, e_idx: {e_idx}")
