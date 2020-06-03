/* This Source Code Form is subject to the terms of the Mozilla Public
* License, v. 2.0. If a copy of the MPL was not distributed with this
* file, You can obtain one at http://mozilla.org/MPL/2.0/. */

(function() {
    'use strict';

    // move mobile banner up and reveal

    // comparison report

    // animation
    var observer = new IntersectionObserver(
        function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-animated');
                    //entry.unobserve();
                }
            });
        }
    );

    //TODO: check for intersection observer support (and naimation support?)
    document.querySelectorAll('.js-animate').forEach(function(element) {
        var rect = element.getBoundingClientRect();
        var vh = window.innerHeight;
        // TODO: need to take scroll height into account
        // don't want stuff to animate while they're reading
        if(rect.top > vh) {
            element.classList.add('has-animate');
            observer.observe(element);
        }
    });

    // protection report button

})();
