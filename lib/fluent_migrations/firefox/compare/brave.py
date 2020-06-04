from __future__ import absolute_import
import fluent.syntax.ast as FTL
from fluent.migrate.helpers import transforms_from
from fluent.migrate.helpers import VARIABLE_REFERENCE, TERM_REFERENCE
from fluent.migrate import REPLACE, COPY

brave = "firefox/compare/brave.lang"
shared = "firefox/compare/shared.lang"

def migrate(ctx):
    """Migrate bedrock/firefox/templates/firefox/compare/brave.html, part {index}."""

    ctx.add_transforms(
        "firefox/compare/brave.ftl",
        "firefox/compare/brave.ftl",
        [
            FTL.Message(
                id=FTL.Identifier("compare-brave-firefox-vs-brave-which-is"),
                value=REPLACE(
                    brave,
                    "Firefox vs. Brave: Which is the better browser for you?",
                    {
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-compare-brave-to-the-firefox"),
                value=REPLACE(
                    brave,
                    "Compare Brave to the Firefox Browser to find out which is the better browser for you in terms of privacy, utility and portability.",
                    {
                        "Firefox Browser": TERM_REFERENCE("brand-name-firefox-browser"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-comparing-firefox-browser"),
                value=REPLACE(
                    brave,
                    "Comparing Firefox Browser to Brave",
                    {
                        "Firefox Browser": TERM_REFERENCE("brand-name-firefox-browser"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-just-like-the-firefox-browser"),
                value=REPLACE(
                    brave,
                    "Just like the Firefox browser, the Brave browser is free, open source and focused on protecting users’ privacy. Brave is a relative newcomer to the world of browsers: its maker, Brave Software, first debuted the browser in January 2016. In this article we’ll compare our Firefox browser with the Brave browser in three categories: privacy, utility and portability.",
                    {
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-the-brave-browser-like-so"),
                value=REPLACE(
                    brave,
                    "The Brave browser, like so many others, is built on Google’s open-source Chromium code. Open-source means anyone can use the source code and piggy-back on top of it to build whatever they want — like the <a %(opera)s>Opera</a> and <a %(edge)s>Edge</a> browsers. But it doesn’t mean that all Chromium-based browsers are equal or are themselves open source.",
                    {
                        "%%": "%",
                        "%(opera)s": VARIABLE_REFERENCE("opera"),
                        "Opera": TERM_REFERENCE("brand-name-opera"),
                        "%(edge)s": VARIABLE_REFERENCE("edge"),
                        "Edge": TERM_REFERENCE("brand-name-edge"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-brave-differentiates-itself"),
                value=REPLACE(
                    brave,
                    "Brave differentiates itself from the other Chromium browsers by focusing on user privacy — specifically by blocking trackers, scripts, and ads by default. So when you use the Brave browser, the areas of a website that would normally display ads appear as blank spaces. In some instances, pages don’t load properly, which will require you to either choose a different browser or flip the ‘Shields Up’ setting to ‘Shields Down’ which turns off the privacy and security protection.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-the-internet-as-a-whole-is"),
                value=REPLACE(
                    brave,
                    "The Internet as a whole is largely paid for by display advertisements, which keeps the actual content you want to view free. Brave has attempted to upend this model by encouraging its users to opt into Brave’s own reward system, which in reality, is its own ad platform. Once a user has opted-in, Brave will display what they call “privacy-respecting ads” for which you can view and earn what they call a Basic Attention Token a.k.a. a BAT. From this point Brave users can choose to spend their BATs on supporting the sites or individual contributors they love, who in turn can convert the BATs into actual currency.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
        ] + transforms_from("""
compare-brave-whether-this-sounds-complicated = {COPY(brave, "Whether this sounds complicated or like a great idea, probably depends on your level of contempt for the display advertising on the Internet. Most Internet users understand that good content costs money, and are okay with the fact that the money comes from advertising.",)}
""", brave=brave) + [
            FTL.Message(
                id=FTL.Identifier("compare-brave-on-the-other-side-of-the-coin"),
                value=REPLACE(
                    brave,
                    "On the other side of the coin, with the Firefox browser, we prefer to keep things simple. Firefox blocks many third party trackers, cryptominers and fingerprinting trackers from following you by default. However, Firefox, outside of Private Browsing Mode, chooses not to block display ads from appearing. That is, unless you install <a %(attrs)s>one of the extensions specifically designed for that purpose</a>.",
                    {
                        "%%": "%",
                        "%(attrs)s": VARIABLE_REFERENCE("attrs"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-there-are-a-few-of-braves"),
                value=REPLACE(
                    brave,
                    "There are a few of Brave’s security features worth highlighting, such as its automatic HTTPS connection upgrades (which Firefox also offers by <a %(extension)s>extension</a>). Brave and Firefox both offer users a native <a %(lockwise)s>password manager</a> and the ability to check their security statistics anytime. Brave displays stats like the number of trackers it has blocked whenever you open a new tab. Firefox displays similar information when you view <a %(privacy)s>your privacy report</a> which can be accessed anytime by clicking the shield in the address bar.",
                    {
                        "%%": "%",
                        "%(extension)s": VARIABLE_REFERENCE("extension"),
                        "%(lockwise)s": VARIABLE_REFERENCE("lockwise"),
                        "%(privacy)s": VARIABLE_REFERENCE("privacy"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-the-bottom-line-is-that-even"),
                value=REPLACE(
                    brave,
                    "The bottom line is that even though Brave’s revenue model with the Basic Attention Tokens may be too complex for a lot of users, overall both Brave and Firefox browsers offer a variety of ways to enjoy a safe and private browsing experience.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-what-might-surprise-some-new"),
                value=REPLACE(
                    brave,
                    "What might surprise some new Brave users is just how fast pages tend to load in the browser. The reason for these speedy load times is that pages load much quicker when you block all of the advertising on them. There’s simply less to load so it takes less time.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-in-terms-of-actual-precious"),
                value=REPLACE(
                    brave,
                    "In terms of actual precious RAM usage, the Brave browser is much heavier than Firefox. Brave comes pre-loaded with various features and “add-ons” which can be attributed to its usage of more RAM. Firefox, on the other hand, lets you decide which add-ons and extensions you want to bolt on.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-customization-of-ui-elements"),
                value=REPLACE(
                    brave,
                    "Customization of UI elements and themes have been a favorite feature of Firefox users for years and our avid community of developers have created a <a %(addons)s>vast library</a> of open source add-ons and extensions allowing for even more personalization and functionality. Features that come with Firefox when you download include our powerful <a %(screenshot)s>screenshots tool</a>, accessibility features and integration with <a %(pocket)s>Pocket</a> — a resource that lets users quickly save an article for later reading on any device.",
                    {
                        "%%": "%",
                        "%(addons)s": VARIABLE_REFERENCE("addons"),
                        "%(screenshot)s": VARIABLE_REFERENCE("screenshot"),
                        "%(pocket)s": VARIABLE_REFERENCE("pocket"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Pocket": TERM_REFERENCE("brand-name-pocket"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-brave-also-supports-google"),
                value=REPLACE(
                    brave,
                    "Brave also supports Google Chrome’s huge library of extensions available in the Chrome web store and offers a variety of in-browser features like the aforementioned Brave Rewards program, and support for downloading torrents in the browser.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                        "Chrome": TERM_REFERENCE("brand-name-chrome"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-the-ability-to-sync-your-passwords"),
                value=REPLACE(
                    brave,
                    "The ability to sync your passwords, extensions, form data, add-ons and other preferences across all your devices and operating systems is a feature that’s been available for years with Firefox. The synced data is also encrypted, which means no one can access it from the outside.",
                    {
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-the-firefox-browser-also-gives"),
                value=REPLACE(
                    brave,
                    "The Firefox browser also gives users the ability to sign up for a free <a %(accounts)s>Firefox Account</a>. Having a Firefox account is the key to unlocking syncing across devices, plus you get the added benefit of products like <a %(monitor)s>Firefox Monitor</a> which monitors your email addresses and alerts you if any of your information has been involved in any known <a %(breaches)s>data breaches</a>.",
                    {
                        "%%": "%",
                        "%(accounts)s": VARIABLE_REFERENCE("accounts"),
                        "%(monitor)s": VARIABLE_REFERENCE("monitor"),
                        "%(breaches)s": VARIABLE_REFERENCE("breaches"),
                        "Firefox Account": TERM_REFERENCE("brand-name-firefox-account"),
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Firefox Monitor": TERM_REFERENCE("brand-name-firefox-monitor"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-brave-also-recently-gained"),
                value=REPLACE(
                    brave,
                    "Brave also recently gained the ability to sync data across most popular operating systems and devices as well with the added capability of syncing your Basic Attention Tokens.",
                    {
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-when-comparing-the-two-browsers"),
                value=REPLACE(
                    brave,
                    "When comparing the two browsers, both Firefox and Brave offer a sophisticated level of privacy and security by default, available automatically from the very first time you open them.",
                    {
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier("compare-brave-overall-brave-is-a-fast-and"),
                value=REPLACE(
                    brave,
                    "Overall, Brave is a fast, and secure browser, that will have particular appeal to cryptocurrency users but for the vast majority of internet citizens, Firefox remains a better and simpler solution.",
                    {
                        "Firefox": TERM_REFERENCE("brand-name-firefox"),
                        "Brave": TERM_REFERENCE("brand-name-brave"),
                    }
                )
            ),
        ] + transforms_from("""
compare-brave-braves-advertising-replacement = {COPY(brave, "Brave’s advertising replacement idea is a twist on the current model of paid ad placement and paid search. But again, some busy Internet users will probably not want to get too involved with the management of micro payments to sites in exchange for their time and attention.",)}
""", brave=brave)
        )
