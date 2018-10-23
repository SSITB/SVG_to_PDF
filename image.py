from cairosvg import svg2png
svg_code=""" <svg xmlns="http://www.w3.org/2000/svg" width="796.8000000000001" height="988.8000000000001" viewBox="0 0 796.8000000000001 988.8000000000001" x="0" y="0"><g><title>background</title><rect display="inline" fill="#c5e5e5" id="canvas_background" stroke-width="0" height="988.8" width="796.8" y="0" x="0"/></g><g><title>Layer 1</title><g id="svg_1" type="text" text="World Flags" font-size="75.04239" font-family="Afta sans" fill="0" text-anchor="start" font-weight="normal" font-style="normal" lineHeight="1" shapeId="0" shapeVal="0" elemBBoxWidth="398.40005" elemBBoxHeight="76.31808" xscale="1" yscale="1"><path id="svg_2" fill="#000000" stroke-width="0" d="m196.49729,151.35846c0,0 5.55314,0 5.55314,0c0,0 18.16026,49.97823 18.16026,49.97823c0,0 12.90729,-49.97823 12.90729,-49.97823c0,0 6.15348,0 6.15348,0c0,0 12.60712,50.12832 12.60712,50.12832c0,0 17.78505,-50.12832 17.78505,-50.12832c0,0 5.70322,0 5.70322,0c0,0 -19.51102,53.65531 -19.51102,53.65531c0,0 -7.27911,0 -7.27911,0c0,0 -12.38199,-50.95378 -12.38199,-50.95378c0,0 -12.53208,50.95378 -12.53208,50.95378c0,0 -7.27911,0 -7.27911,0c0,0 -19.88623,-53.65531 -19.88623,-53.65531m87.04917,34.06924c0,16.43428 7.57928,17.40983 13.20746,17.40983c4.35246,0 12.00678,-0.07504 12.00678,-17.40983c0,-16.8095 -7.72937,-16.95958 -12.83225,-16.95958c-5.17792,0 -12.38199,-0.22513 -12.38199,16.95958c0,0 0,0 0,0m12.38199,-20.41153c14.40814,0 18.46043,9.23021 18.46043,20.41153c0,13.58267 -3.9022,20.86178 -17.63496,20.86178c-13.73276,0 -18.38539,-9.75551 -18.38539,-20.86178c0,-13.05738 4.50254,-20.41153 17.55992,-20.41153c0,0 0,0 0,0m32.0431,39.99759c0,0 -5.17792,0 -5.17792,0c0,0 0,-38.79692 0,-38.79692c0,0 4.12733,0 4.12733,0c0,0 1.05059,8.55483 1.05059,8.55483c2.02614,-5.17792 4.50254,-9.68047 10.88115,-9.68047c3.22682,0 5.02784,0.60034 6.00339,0.97555c0,0 -0.30017,4.12733 -0.30017,4.12733c-2.92665,-0.90051 -3.97725,-1.20068 -5.70322,-1.20068c-5.10288,0 -10.88115,4.4275 -10.88115,17.40983c0,0 0,18.61051 0,18.61051c0,0 0,0 0,0m28.36602,0c0,0 -4.9528,0 -4.9528,0c0,0 0,-59.58366 0,-59.58366c0,0 4.9528,0 4.9528,0c0,0 0,59.58366 0,59.58366c0,0 0,0 0,0m37.07094,-16.65941c0,0 0.07504,-16.95958 0.07504,-16.95958c-2.62648,-1.20068 -8.77996,-3.22682 -12.53208,-3.22682c-10.58098,0 -10.35585,13.58267 -10.35585,17.18471c0,6.3786 1.05059,17.25975 9.9056,17.25975c9.00509,0 12.90729,-5.02784 12.90729,-14.25805c0,0 0,0 0,0m0.07504,11.55653c-2.32631,3.52699 -6.67877,6.00339 -12.98233,6.00339c-8.10458,0 -14.93344,-5.17792 -14.93344,-20.48657c0,-15.00848 7.35415,-20.7117 15.38369,-20.7117c2.62648,0 7.20407,0.67538 12.53208,2.70153c0,0 0,-21.91238 0,-21.91238c0,0 5.02784,0 5.02784,0c0,0 0,59.80878 0,59.80878c0,0 -4.72767,0 -4.72767,0c0,-0.97555 -0.30017,-1.50085 -0.30017,-5.40305c0,0 0,0 0,0m36.77077,5.10288c0,0 0,-53.58027 0,-53.58027c0,0 34.66958,0 34.66958,0c0,0 0,3.30187 0,3.30187c0,0 -29.86687,0 -29.86687,0c0,0 0,21.38708 0,21.38708c0,0 18.53547,0 18.53547,0c0,0 0,3.75212 0,3.75212c0,0 -18.53547,0 -18.53547,0c0,0 0,25.1392 0,25.1392c0,0 -4.80271,0 -4.80271,0c0,0 0,0 0,0m48.25226,0c0,0 -4.9528,0 -4.9528,0c0,0 0,-59.58366 0,-59.58366c0,0 4.9528,0 4.9528,0c0,0 0,59.58366 0,59.58366c0,0 0,0 0,0m31.81797,-7.35415c0,0 0.15008,-13.13242 0.15008,-13.13242c-4.50254,1.12564 -7.27911,1.12564 -10.65602,1.12564c-3.60203,0 -8.17962,-0.07504 -8.17962,8.32971c0,10.95619 12.90729,9.98064 18.68555,3.67708c0,0 0,0 0,0m5.02784,-17.48488c0,0 0,24.83903 0,24.83903c0,0 -3.52699,0 -3.52699,0c0,0 -2.4764,-2.77657 -2.4764,-2.77657c-3.45195,1.80102 -6.67877,3.30187 -12.83225,3.30187c-5.77826,0 -9.83055,-4.05229 -9.83055,-11.63157c0,-6.00339 2.77657,-11.48149 12.08182,-11.48149c7.65432,0 9.3803,0 11.55653,-2.02614c0,-10.65602 -2.17623,-11.78166 -8.70492,-11.78166c-5.17792,0 -8.77996,1.35076 -11.10627,2.25127c-0.5253,-1.42581 -0.67538,-2.02614 -1.27572,-3.30187c11.10627,-3.9022 26.11475,-6.00339 26.11475,12.60712c0,0 0,0 0,0m12.23191,32.34327c2.92665,2.92665 6.60373,5.92835 12.00678,5.92835c12.90729,0 12.68216,-10.50593 12.68216,-12.98233c0,0 0,-4.87776 0,-4.87776c-2.92665,4.12733 -5.92835,5.85331 -11.8567,5.85331c-13.58267,0 -18.08522,-10.13072 -18.08522,-21.16195c0,-12.90729 4.4275,-20.26145 17.33479,-20.26145c7.57928,0 10.8061,2.25127 13.8078,6.82886c0,0 0.37521,-5.70322 0.37521,-5.70322c0,0 3.37691,0 3.37691,0c0,0 0,39.32221 0,39.32221c0,2.4764 -0.07504,16.2842 -17.63496,16.2842c-6.67877,0 -11.40644,-2.62648 -15.00848,-6.82886c0,0 3.0017,-2.40136 3.0017,-2.40136m-0.22513,-27.24039c0,16.20916 7.57928,17.71 13.05738,17.71c4.35246,0 11.93174,-0.60034 11.93174,-17.71c0,-16.50933 -7.12903,-16.73445 -12.15687,-16.73445c-5.17792,0 -12.83225,-0.30017 -12.83225,16.73445c0,0 0,0 0,0m51.10387,-19.88623c6.82886,0 11.63157,2.32631 14.40814,3.52699c0,1.12564 0.07504,2.62648 0.07504,3.60203c-4.87776,-2.10119 -9.3803,-3.97725 -14.48318,-3.97725c-3.97725,0 -8.10458,0.90051 -8.10458,6.67877c0,4.80271 2.77657,5.85331 8.77996,7.35415c10.58098,2.70153 15.7589,6.00339 15.7589,12.08182c0,7.20407 -6.22852,11.48149 -15.38369,11.48149c-7.80441,0 -13.50763,-3.07674 -15.38369,-4.35246c0,-1.72597 0.07504,-3.15178 0.07504,-4.87776c4.57759,2.70153 9.68047,5.47809 15.30865,5.47809c5.32801,0 10.13072,-1.50085 10.13072,-7.72937c0,-5.10288 -6.45365,-6.75382 -13.95788,-8.855c-8.25466,-2.32631 -10.65602,-5.55314 -10.65602,-10.73106c0,-3.60203 2.25127,-9.68047 13.43259,-9.68047c0,0 0,0 0,0"/><rect id="svg_3" x="196.49728" y="145.43011" width="398.40005" height="76.31808" fill="#000000" opacity="0"/></g><g id="svg_15"><rect id="svg_14" x="80.28107" fill="#FF0000" width="66.89096" height="132.64306" y="352.40187"/><rect id="svg_13" x="147.17389" y="440.5012" width="200.66729" height="44.54559"/><rect id="svg_12" x="147.17389" y="397.14285" fill="#FFFFFF" width="200.66729" height="43.95197"/><rect id="svg_11" x="147.17389" fill="#009A00" width="200.66729" height="44.74098" y="352.40187"/></g><g id="svg_21"><rect id="svg_20" x="524.35134" y="349.21537" fill="#FFFFFF" width="131.38735" height="130.90984"/><path fill="#BF0A30" d="m458.6595,349.21537l65.69551,0l0,130.90984l-65.69551,0l0,-130.90984zm197.07918,0l65.69367,0l0,130.90984l-65.69367,0l0,-130.90984zm-111.73801,63.2584l-5.10196,1.23049l23.73935,14.68512c1.79615,3.7778 -0.62259,4.89075 -2.1653,6.86873l25.77058,-2.30672l-0.67034,18.28477l5.3352,-0.11019l-1.16254,-18.13234l25.79996,2.15612c-1.59597,-2.37467 -3.0193,-3.63638 -1.54271,-7.4399l23.72465,-13.9156l-4.15246,-1.05969c-3.39396,-1.84758 1.46557,-8.89629 2.2002,-13.34076c0,0 -13.85132,3.35723 -14.75858,1.59964l-3.52619,-4.77689l-12.6043,9.75763c-1.37558,0.23324 -1.96328,-0.15243 -2.28835,-0.97338l5.82556,-20.39314l-9.22136,3.65475c-0.77135,0.23141 -1.54271,0.03122 -2.05511,-0.60239l-8.8669,-12.54369l-9.14238,13.02854c-0.69055,0.46649 -1.37925,0.51975 -1.95226,0.20202l-8.77691,-3.47109l5.26908,20.23336c-0.42057,0.80441 -1.42517,1.03031 -2.60608,0.59688l-12.04598,-9.64927c-1.57577,1.77779 -2.64464,4.68873 -4.72546,5.34071c-2.08449,0.60974 -9.06158,-1.23417 -13.73562,-1.95226c1.59597,4.06063 6.59141,10.81549 3.43069,13.03038l0.00551,-0.00184l0,0l0.00001,0.00001z" id="svg_22"/></g><g id="svg_34"><rect id="svg_33" x="285.68647" y="571.02527" fill="#00CC00" width="257.07968" height="127.83057"/><rect id="svg_32" x="285.68647" y="571.02527" fill="#6699FF" width="257.07968" height="63.91528"/><path id="svg_31" fill="#FFFEFE" d="m285.68647,571.02527l95.55371,63.83458l-95.55371,63.7485l0,-127.58308z"/><path id="svg_30" fill="#FF0000" d="m325.5851,643.9468l-7.6953,-5.5361l-7.65585,5.59169l2.84606,-9.09053l-7.64509,-5.61321l9.45638,-0.07711l2.93214,-9.06184l2.99491,9.04032l9.45638,0.01435l-7.60384,5.66343l2.91062,9.0726l0.00359,-0.00359l0,0l0,-0.00001z"/></g><text fill="#000000" stroke="#000000" stroke-width="0" x="71.62903" y="303.01305" id="svg_35" font-size="24" font-family="Afta sans" text-anchor="middle" xml:space="preserve" isvdp="true" transform="matrix(2.20606 0 0 2.20606 137.937 209.761)">Contact Number</text></g><g><title>Border</title><rect fill="none" id="canvas_border" stroke-width="0" stroke="#000" height="960" width="768" y="0" x="0"/></g><g><title>Overlay</title></g></svg>
"""
svg2png(bytestring=svg_code,write_to='output.png')