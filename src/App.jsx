import React from 'react';
import './index.css';
import Logo from "./assets/infabio-logo.png";
import PaidAdImg from "./assets/paid_advertising.png";
import SeoImg from "./assets/seo.png";
import CroImg from "./assets/cro.png";
import EmailImg from "./assets/email_marketing.png";

function App() {
  return (
    <>
      {/* Navbar */}
      <nav style={{ borderBottom: '3px solid var(--border-color)', padding: '1.25rem 0', backgroundColor: '#FFF', position: 'sticky', top: 0, zIndex: 100 }}>
        <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <img src={Logo} alt="Infabio Logo" style={{ height: '40px' }} />
          </div>
          <div className="nav-links" style={{ display: 'flex', gap: '2.5rem', alignItems: 'center', fontWeight: 700, fontSize: '1rem', textTransform: 'uppercase' }}>
            <a href="#services" style={{ color: 'var(--text-main)', textDecoration: 'none' }}>Services</a>
            <a href="#results" style={{ color: 'var(--text-main)', textDecoration: 'none' }}>Results</a>
            <a href="#about" style={{ color: 'var(--text-main)', textDecoration: 'none' }}>About</a>
            <a href="#case-studies" style={{ color: 'var(--text-main)', textDecoration: 'none' }}>Case Studies</a>
            <a href="#contact" className="btn">Free Marketing Plan</a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="section" style={{ overflow: 'hidden' }}>
        <div className="container grid-2">
          <div>
            <h1 style={{ fontSize: '4rem', lineHeight: '1.1' }}>
              We Tie Your <span className="highlight">Financial Goals</span> To Marketing Growth
            </h1>
            <p style={{ fontSize: '1.25rem', marginBottom: '2rem', maxWidth: '90%' }}>
              Is your current budget allocation the best? Where should you spend your next dollar? We’ll show you exactly how to scale without wasting ad spend.
            </p>
            <div style={{ display: 'flex', gap: '1.5rem', alignItems: 'center' }}>
              <a href="#contact" className="btn" style={{ fontSize: '1.25rem', padding: '1rem 2rem' }}>Get Your Free Plan</a>
              <span className="handwritten-note">Wait, it's really free? 😱</span>
            </div>
          </div>
          <div style={{ position: 'relative', perspective: '1000px' }}>
            {/* Mock Dashboard Card */}
            <div className="card" style={{ padding: '0', overflow: 'hidden', transform: 'rotateY(-15deg) rotateX(5deg)', boxShadow: '12px 12px 0px var(--shadow-color)' }}>
              <div style={{ backgroundColor: 'var(--secondary)', color: 'white', padding: '1rem', display: 'flex', alignItems: 'center', borderBottom: '3px solid var(--secondary)' }}>
                <div style={{ display: 'flex', gap: '8px' }}>
                  <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#FF5F56', border: '2px solid rgba(0,0,0,0.2)' }}></div>
                  <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#FFBD2E', border: '2px solid rgba(0,0,0,0.2)' }}></div>
                  <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#27C93F', border: '2px solid rgba(0,0,0,0.2)' }}></div>
                </div>
                <div style={{ marginLeft: '1.5rem', opacity: 0.9, fontSize: '0.9rem', fontFamily: 'monospace', fontWeight: 'bold' }}>infabio-growth-dashboard.app</div>
              </div>
              <div style={{ padding: '2rem', backgroundColor: '#F8FAFC' }}>
                <div style={{ height: '48px', backgroundColor: 'var(--bg-light)', border: '3px solid var(--secondary)', marginBottom: '1.5rem', borderRadius: '4px', display: 'flex', alignItems: 'center', padding: '0 1rem' }}>
                  <span style={{ fontWeight: 'bold', color: 'var(--secondary)' }}>Revenue Growth ↑ +63%</span>
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
                  <div style={{ height: '140px', backgroundColor: 'var(--primary)', border: '3px solid var(--secondary)', borderRadius: '4px', boxShadow: '4px 4px 0px var(--secondary)' }}></div>
                  <div style={{ height: '140px', backgroundColor: '#FFBD2E', border: '3px solid var(--secondary)', borderRadius: '4px', boxShadow: '4px 4px 0px var(--secondary)' }}></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Logos Section */}
      <section className="section-light" style={{ padding: '4rem 0' }}>
        <div className="container" style={{ textAlign: 'center' }}>
          <p style={{ fontWeight: 800, color: 'var(--secondary)', marginBottom: '3rem', letterSpacing: '2px', textTransform: 'uppercase' }}>Trusted By Industry Leaders</p>
          <div style={{ display: 'flex', justifyContent: 'center', gap: '5rem', flexWrap: 'wrap', opacity: 0.4 }}>
            {/* Simple typography-based dummy logos */}
            <h2 style={{ margin: 0, color: '#000', fontSize: '2rem' }}>Segment</h2>
            <h2 style={{ margin: 0, color: '#000', fontSize: '2rem', fontStyle: 'italic' }}>Lytx</h2>
            <h2 style={{ margin: 0, color: '#000', fontSize: '2rem', textTransform: 'uppercase' }}>Wunderkind</h2>
            <h2 style={{ margin: 0, color: '#000', fontSize: '2rem', letterSpacing: '-2px' }}>Justworks</h2>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="section" style={{ backgroundColor: '#F0F4F8' }}>
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: '850px', margin: '0 auto 5rem' }}>
             <p style={{ fontWeight: 800, color: 'var(--secondary)', marginBottom: '1rem', letterSpacing: '2px', textTransform: 'uppercase', fontSize: '0.9rem' }}>Our Expertise</p>
            <h2 style={{ fontSize: '3.5rem' }}>Have all your marketing pull in the same direction, while capitalizing on every opportunity.</h2>
          </div>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4rem', alignItems: 'center' }}>
            {/* Paid Advertising Card */}
            <div className="card" style={{ maxWidth: '900px', width: '100%', padding: '4rem', textAlign: 'center' }}>
              <h3 style={{ fontSize: '2.5rem', marginBottom: '1.5rem' }}>Paid Advertising</h3>
              <p style={{ fontSize: '1.25rem', maxWidth: '800px', margin: '0 auto 3rem' }}>
                Improve the performance of your paid social, paid search, PPC, SEM, and eCommerce ad campaigns. It's what we built our reputation on.
              </p>
              <img src={PaidAdImg} alt="Paid Advertising Illustration" style={{ width: '100%', maxWidth: '600px', height: 'auto', margin: '0 auto' }} />
            </div>

            {/* SEO Card */}
            <div className="card" style={{ maxWidth: '900px', width: '100%', padding: '4rem', textAlign: 'center' }}>
              <h3 style={{ fontSize: '2.5rem', marginBottom: '1.5rem' }}>Search Engine Optimization</h3>
              <p style={{ fontSize: '1.25rem', maxWidth: '800px', margin: '0 auto 3rem' }}>
                Rise in organic search and reach the first page as we'll get your higher quality backlinks with content marketing & higher-converting website traffic.
              </p>
              <img src={SeoImg} alt="SEO Illustration" style={{ width: '100%', maxWidth: '600px', height: 'auto', margin: '0 auto' }} />
            </div>

            {/* CRO Card */}
            <div className="card" style={{ maxWidth: '900px', width: '100%', padding: '4rem', textAlign: 'center' }}>
              <h3 style={{ fontSize: '2.5rem', marginBottom: '1.5rem' }}>Conversion Rate Optimization</h3>
              <p style={{ fontSize: '1.25rem', maxWidth: '800px', margin: '0 auto 3rem' }}>
                Increase your conversion rates to lower your cost per conversion and get a higher conversion volume. All leading to more revenue as well.
              </p>
              <img src={CroImg} alt="CRO Illustration" style={{ width: '100%', maxWidth: '600px', height: 'auto', margin: '0 auto' }} />
            </div>

            {/* Email Marketing Card */}
            <div className="card" style={{ maxWidth: '900px', width: '100%', padding: '4rem', textAlign: 'center' }}>
              <h3 style={{ fontSize: '2.5rem', marginBottom: '1.5rem' }}>Email Marketing</h3>
              <p style={{ fontSize: '1.25rem', maxWidth: '800px', margin: '0 auto 3rem' }}>
                From complex eCommerce email sequences to creative B2B cold outbound email marketing, you'll drive more ROI from your marketing.
              </p>
              <img src={EmailImg} alt="Email Marketing Illustration" style={{ width: '100%', maxWidth: '600px', height: 'auto', margin: '0 auto' }} />
            </div>
          </div>
        </div>
      </section>

      {/* Social Proof Section */}
      <section id="results" className="section section-light" style={{ overflow: 'hidden' }}>
        <div className="container">
          <div className="grid-2">
            <div style={{ zIndex: 10 }}>
              <h2 style={{ fontSize: '3.5rem', lineHeight: 1.1, marginBottom: '2rem' }}>More <span className="highlight">Success Stories</span> Than Other Agencies Have Clients</h2>
              <p style={{ fontSize: '1.25rem', marginBottom: '2.5rem' }}>We help scrappy startups to massive brands, from straightforward products to ultra-complex services.</p>
              <a href="#contact" className="btn btn-secondary" style={{ fontSize: '1.25rem', padding: '1rem 2rem' }}>See All Case Studies</a>
              <div className="handwritten-note" style={{ display: 'block', marginTop: '2rem' }}>
                We got unlimited references for you to talk to too 😍 ↘
              </div>
            </div>
            <div style={{ position: 'relative', height: '500px' }}>
              {/* Stacked polaroids/cards */}
              <div className="card" style={{ position: 'absolute', top: '10px', right: '40px', width: '280px', transform: 'rotate(8deg)', zIndex: 1, padding: '1rem' }}>
                <div style={{ backgroundColor: '#E2E8F0', height: '200px', marginBottom: '1.5rem', border: '3px solid var(--secondary)' }}></div>
                <p style={{ fontStyle: 'italic', fontSize: '1.1rem', marginBottom: '1rem', color: '#000', fontWeight: 'bold' }}>"Infabio completely transformed our ROI. The transparency is unmatched."</p>
                <strong>- Sarah J., CMO at TechFlow</strong>
              </div>
              <div className="card" style={{ position: 'absolute', top: '60px', right: '180px', width: '280px', transform: 'rotate(-6deg)', zIndex: 2, padding: '1rem' }}>
                <div style={{ backgroundColor: '#CBD5E1', height: '200px', marginBottom: '1.5rem', border: '3px solid var(--secondary)' }}></div>
                <p style={{ fontStyle: 'italic', fontSize: '1.1rem', marginBottom: '1rem', color: '#000', fontWeight: 'bold' }}>"This is the only marketing agency with aggressive accountability."</p>
                <strong>- Mike T., Founder at GrowthScale</strong>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA / Footer */}
      <section id="contact" className="section" style={{ backgroundColor: 'var(--secondary)', color: 'white', padding: '8rem 0' }}>
        <div className="container" style={{ textAlign: 'center' }}>
          <h2 style={{ color: 'white', fontSize: '4.5rem', marginBottom: '1.5rem' }}>Ready To Hit <span style={{ backgroundColor: 'var(--primary)', padding: '0 0.5rem', transform: 'rotate(2deg)', display: 'inline-block', border: '4px solid #FFF', boxShadow: '6px 6px 0px #000' }}>Target Goals?</span></h2>
          <p style={{ color: '#E2E8F0', fontSize: '1.5rem', maxWidth: '700px', margin: '0 auto 3rem' }}>
            Stop guessing and start scaling. Get your free custom marketing performance plan today. We do the math, you see the growth.
          </p>
          <button className="btn" style={{ fontSize: '1.5rem', padding: '1.25rem 3rem', boxShadow: '8px 8px 0px #0F2032' }}>Get My Free Proposal</button>
        </div>
      </section>
      
      <footer style={{ backgroundColor: '#7ea474', color: '#FFFFFF', padding: '5rem 0 3rem', position: 'relative' }}>
        <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '8px', backgroundColor: '#1D3B5A' }}></div>

        <div className="container">
          <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr 1fr 1.5fr', gap: '4rem', marginBottom: '5rem', textAlign: 'left' }}>
            {/* Column 1: Brand */}
            <div>
              <div style={{ marginBottom: '1.5rem' }}>
                <img src={Logo} alt="Infabio Logo" style={{ height: '40px', filter: 'brightness(0) invert(1)' }} />
              </div>
              <p style={{ color: 'rgba(255,255,255,0.8)', fontSize: '1rem', lineHeight: '1.6', marginBottom: '2rem' }}>
                AI-powered marketing defense system protecting brands from budget waste and maximizing ROI across three continents.
              </p>
              <div style={{ display: 'flex', gap: '1rem' }}>
                 {['in', 'tw', 'ig'].map(network => (
                    <a href="#" key={network} style={{ width: '40px', height: '40px', borderRadius: '4px', border: '2px solid #FFFFFF', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#FFFFFF', textDecoration: 'none', fontSize: '0.9rem', fontWeight: 'bold' }}>
                      {network}
                    </a>
                  ))}
              </div>
            </div>

            {/* Column 2: Services */}
            <div>
              <h4 style={{ color: '#FFFFFF', fontWeight: 800, marginBottom: '1.5rem', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>Services</h4>
              <nav style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                {['AI Media Buying', 'SEO & Search', 'Conversion Optimization', 'Social Media', 'Email Marketing', 'Brand Protection'].map(link => (
                  <a href="#" key={link} style={{ color: 'rgba(255,255,255,0.8)', textDecoration: 'none', fontSize: '0.95rem' }}>{link}</a>
                ))}
              </nav>
            </div>

            {/* Column 3: Company */}
            <div>
              <h4 style={{ color: '#FFFFFF', fontWeight: 800, marginBottom: '1.5rem', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>Company</h4>
              <nav style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                {['About Us', 'Case Studies', 'Insights', 'Careers', 'Contact'].map(link => (
                  <a href="#" key={link} style={{ color: 'rgba(255,255,255,0.8)', textDecoration: 'none', fontSize: '0.95rem' }}>{link}</a>
                ))}
              </nav>
            </div>

            {/* Column 4: Global Presence */}
            <div>
              <h4 style={{ color: '#FFFFFF', fontWeight: 800, marginBottom: '1.5rem', textTransform: 'uppercase', fontSize: '0.9rem', letterSpacing: '1px' }}>Global Presence</h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'flex-start' }}>
                  <div style={{ marginTop: '0.2rem' }}>📍</div>
                  <div>
                    <h5 style={{ color: '#FFFFFF', margin: 0, fontSize: '1rem' }}>Gurugram, India</h5>
                    <p style={{ margin: 0, color: 'rgba(255,255,255,0.6)', fontSize: '0.85rem' }}>Defense Command Center</p>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'flex-start' }}>
                  <div style={{ marginTop: '0.2rem', color: '#FFBD2E' }}>📍</div>
                  <div>
                    <h5 style={{ color: '#FFFFFF', margin: 0, fontSize: '1rem' }}>Jaipur, India</h5>
                    <p style={{ margin: 0, color: 'rgba(255,255,255,0.6)', fontSize: '0.85rem' }}>Creative Division</p>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'flex-start' }}>
                  <div style={{ marginTop: '0.2rem', color: '#C0DEF7' }}>📍</div>
                  <div>
                    <h5 style={{ color: '#FFFFFF', margin: 0, fontSize: '1rem' }}>New York, USA</h5>
                    <p style={{ margin: 0, color: 'rgba(255,255,255,0.6)', fontSize: '0.85rem' }}>Global Expansion HQ</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '3rem', borderTop: '1px solid rgba(255,255,255,0.1)', flexWrap: 'wrap', gap: '2rem' }}>
            <div style={{ display: 'flex', gap: '2rem', alignItems: 'center' }}>
              <a href="mailto:contact@marketingdefense.com" style={{ color: 'rgba(255,255,255,0.8)', textDecoration: 'none', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                ✉ contact@marketingdefense.com
              </a>
              <span style={{ color: 'rgba(255,255,255,0.4)', fontSize: '0.9rem' }}>© 2026 Marketing Defense. All rights reserved.</span>
            </div>
            <div style={{ display: 'flex', gap: '2rem' }}>
              {['Privacy Policy', 'Terms of Service', 'Cookie Policy'].map(link => (
                <a href="#" key={link} style={{ color: 'rgba(255,255,255,0.8)', textDecoration: 'none', fontSize: '0.9rem' }}>{link}</a>
              ))}
            </div>
          </div>
        </div>
      </footer>
    </>
  )
}

export default App;
