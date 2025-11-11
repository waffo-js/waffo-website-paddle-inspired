---
title: "External payments for iOS: How app developers are responding in a post-Epic vs. Apple world"
description: "Nathan Hudson and Lucas Lovell discuss external payments strategies, optimization tips, and technical considerations following the Epic vs. Apple ruling."
source: "resources/external-payments-guide-ios-app-developers.html"
---

# External payments for iOS: How app developers are responding in a post-Epic vs. Apple world

Following the Epic vs. Apple ruling, we look at how developers can capitalize on the new opportunities on offer. 

  * [The current lay of the land](#lay-of-land)
  * [Implementation options](#technical)
  * [Key success factors and optimization strategies](#optimization-strategies)
  * [Implementation strategy and rollout plan](#Implementation-strategy-and-rollout-plan)
  * [Challenges and mitigation strategies](#Challenges-mitigation-strategies)
  * [Ready to rise to the opportunity?](#Read-to-rise-to-the-oppurtunity)


Share

[](https://x.com/intent/tweet?text=External%20payments%20for%20iOS%3A%20How%20app%20developers%20are%20capitalizing%20on%20new%20opportunities%20-%20https%3A%2F%2Fwww.paddle.com%2Fresources%2Fexternal-payments-guide-ios-app-developers%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fresources%2Fexternal-payments-guide-ios-app-developers)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fresources%2Fexternal-payments-guide-ios-app-developers&title=External%20payments%20for%20iOS%3A%20How%20app%20developers%20are%20capitalizing%20on%20new%20opportunities&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

The mobile app market is experiencing a seismic shift with the recent Epic vs. Apple ruling.

With no Apple fees or restrictions on linking out to external payments, this landmark decision effectively allows developers to bypass the 15-30% commission on in-app purchases, creating unprecedented opportunities to grow revenue and margins. 

This ruling affects over 118,000 apps developed in the US, as well as any app selling into the US market. 

These developers now face a critical strategic decision: whether to implement external payment options, and if so, how to optimize the user experience to maximize conversion rates while maintaining user trust. 

We brought in App Marketer of the Year, Nathan Hudson, and Lucas Lovell, VP of Product at Paddle, to look at where the opportunities lie today and what companies are doing. This playbook provides insights from early adopters and practical recommendations to help navigate this new world confidently. 

**[Watch the full conversation here](https://www.paddle.com/events/webinars/web-revenue-labs-what-to-do-in-this-post-apple-ruling-landscape).**

## The current (legal) lay of the land

First, let’s clarify what this legislation actually means.

The recent ruling establishes several key principles that app developers should understand:

**Universal application** : The ruling applies to all apps, not just "reader apps".

Any app selling anything with a payment can implement alternative methods, including both subscription and consumable purchase apps.

**Legal protection** : The court explicitly prohibits Apple from retaliating against developers who implement alternative payment methods, providing a safeguard for businesses exploring these options.

**User communication freedom** : The ruling prevents Apple from using scare tactics to discourage users from choosing alternative payment options, allowing developers to communicate openly with their customers.

The ruling has created serious noise in the market, but what does sentiment look like? Lucas and Nathan break things down in the video below.

## Can I really trust these new changes?

Even after the ruling, some developers we’ve spoken to are cautious to engage with external payments, fearful of App Store penalties. 

But Apple execs are (potentially) facing criminal proceedings after violating a 2021 ruling, and could face prison time if the same judge believes they are still acting in bad faith later down the line. 

Additionally, Apple had their appeal to pause external payments momentarily rejected by a U.S appeals caught on June 4th. It is therefore highly unlikely Apple will punish any app making the most out of this newfound opportunity. 

**[Read more about the landmark decision here](https://www.paddle.com/blog/apple-vs-epic-app-store-changes).**

## **The ruling for mobile apps in the Small Business Program**

For those on Apple’s small business program, the financial incentives are definitely less dramatic than for larger apps paying Apple’s full fee. But even for these sellers, there are still some notable benefits. 

### **Cash flow advantages for growing apps**

Small business apps often face significant cash flow challenges when scaling their marketing efforts. 

Apple's payout delays of up to 60 days can severely limit a growing app's ability to reinvest in user acquisition, especially when trying to establish their first profitable marketing channel.

External payments solve this immediately. Instead of waiting two months for revenue, developers can access funds within weeks, allowing for more aggressive testing and iteration cycles that are critical during the growth phase

## Breaking down the implementation options

What does this all mean in practice?

How can apps carry out the technical implementation today? 

At its foundation, implementing external payments involves four fundamental steps:

  1. Adding a button to your paywall directing users to an external payment.
  2. Creating a [website checkout](https://www.paddle.com/billing/checkout) experience.
  3. Redirecting users back to the app after purchase completion.
  4. Handling fulfilment to unlock the features bought.


This journey from the app to the web (to purchase) has been coined **App2Web** , and one app company capitalizing on the new motion successfully is [Stoikk](https://www.stoikk.com/).

## No drop in conversions, launched in days: Stoikk's success so far

When the ruling was announced, Stoikk saw a huge opportunity to keep more of its revenue but knew they had to act fast.

**"Appeal processes in the US can take six to eight months, so we saw this as a short window of opportunity. It made strategic sense to be among the first movers."**  
**-** Erkmen Erakkus, Co-Founder and CEO, Stoikk

Here's how they established their new App2Web monetization strategy successfully: 

**Dual options to highlight the benefit for the user** : 

Their paywall features two call-to-action buttons: "Use Apple Pay and get a 25% extra discount" and "Continue in-app."

**Apple Pay focus**

Their checkout design prioritized Apple Pay over credit/debit card payment to maintain the familiarity and trust of the native payment experience.

**Trust signaling**

They implemented a loading screen with their app logo before the checkout page to reinforce user trust and brand recognition.

Their experience executing web funnels previously provided them with valuable data on higher lifetime values (LTVs) with web payments, allowing them to make informed decisions about their implementation strategy.

**No drop in conversions**

The early results have been promising. 

Early data shows that rather than a dip in conversions, Stoikk has seen a slight uplift. 

The company anticipates significant increases in customer lifetime value through improved retention tactics available with web payments, and by moving quickly, they've gained valuable insights before the market becomes saturated and CPMs (Cost Per Mille) potentially increase.

### **RevenueCat's Dipsea experiment**

RevenueCat's aggregate data shows that while some apps experience initial conversion dips of 10-15% when implementing external payments, others see improvements. 

The difference often comes down to implementation sophistication and audience alignment.

Having acquired romantic audiobook app Dipsea last year, RevenueCat have been able to run a number of first hand experiments with an App2Web motion. 

Dipsea’s users required particularly careful trust-building due to the sensitive nature of their product.

They implemented a "content preview" approach where users sample the experience before being presented with payment options, building confidence in the value proposition. 

For Dipsea, the auto-renewal challenge was particularly important given their subscription model, requiring significant investment in robust renewal infrastructure and proactive subscriber communication.

The results have been promising, maintaining strong conversion rates while significantly improving their unit economics through reduced platform fees.  


### **The experimental setup**

The experiment tested four distinct approaches: 

  * Variant A: Original native paywall with IAP only 
  * Variant B: Functionally identical IAP-only paywall (a control to ensure their implementation didn’t introduce issues)
  * Variant C: Choice between in-app purchase and discounted web payment
  * Variant D: Web payment only


### **Conversion patterns and the friction paradox**

The data revealed an interesting pattern. While external payments showed a significant drop in initial trial starts when users moved from app to web, the complete funnel told a different story. The conversion rate from trial to paid subscription was substantially higher for web payments.

This suggests that the higher friction of web checkout actually filters for higher-intent users from the start. 

Despite fewer people starting trials, more of those who do start end up converting to paid subscriptions.

### **Revenue parity despite fee differences**

External payments achieved near-parity with in-app purchases when accounting for platform fees.

With web payments costing approximately 6% versus Apple's 30% commission, the revenue per customer proved almost equivalent, making the switch financially neutral in the short term.

### **The retention advantage**

Among 2,000 active subscriptions initiated in May, only 2.5% of web payment subscribers had turned off auto-renewal, compared to 18% of App Store subscribers who had already disabled auto-renewal.

This retention difference suggests that while first-year revenues might be comparable, web payments could provide significant long-term revenue advantages, potentially improving lifetime value by 15-20%.

The auto-renewal infrastructure challenge proved particularly important for Dipsea's subscription model, requiring significant investment in robust renewal systems and proactive subscriber communication. However, this upfront investment enabled the superior retention rates that drive long-term value.

Additional data from other companies reinforces these patterns, with some reporting 10-15% conversion drops offset by 2-3x improvements in trial-to-paid conversion rates on web platforms. 

## Key success factors and optimization strategies

Not everyone has found success.

Although the early signs are positive for Stoikk, others in the space, like **[Superwall](https://superwall.com/blog/initial-data-is-in-app-to-web-conversion-rates-after-the-app-store-ruling),** who have taken an aggregate of data from their customers, are seeing a drop in conversion (despite an increase in total revenue). 

These dips in conversion and Stoikk's success are relative to the product and the audience.

Outside of the app context, we know from our own tests that a one-page checkout can dramatically increase conversions for inexpensive digital products, but can decrease the conversion rate on pricier B2B SaaS checkout pages. 

Your customer base will have vastly different pay preferences, even from your competitors. Assume nothing and experiment with everything. 

### **A/B testing framework for external payments**

Developers can run A/B tests and segment portions of their audience, even down to specific demographics within the US. Specific test variables to consider include:

  * Price points and discount strategies
  * Placement of the external payment option (paywall vs. earlier in the user journey)
  * Different UX patterns and visuals
  * Various cohorts based on user demographics or behavior


### **Strategic placement beyond paywalls**

While most implementations focus on paywall integration, a more innovative approach involves finding the optimal point in an onboarding journey to link users to web-based payments. 

By strategically timing when users are directed to web payments, developers may significantly reduce conversion friction.

This could involve initiating onboarding in the app, then transitioning to web during a loading screen or interstitial moment when customizing plans, creating a more natural flow in the user journey.

### **Building user trust**

The payment experience serves as a reflection of the trust users have in your service. Effective design isn't just about aesthetics, it's about fostering and maintaining user confidence throughout the payment process.

Practical trust-building elements include:

  * Brand-consistent loading screens
  * Simplified and trusted payment options (preferably Apple Pay)
  * Clear communication about the payment process
  * Visual consistency between app and web experiences


### **Retention optimization**

Beyond initial conversion, the ruling unlocks significant advantages for customer retention. Apps are now free to communicate with customers about their subscriptions and payments, meaning you can inform users about failed payments (and get them to update details) or serve up discounts. 

**Advanced cancellation flows**

Unlike Apple's streamlined cancellation process, web payments allow for implementing sophisticated cancellation flows with a range of options.****

When a customer goes to cancel, you can show a form asking why they're cancelling and then present offers based on their answers. 

For example, you could present a discount to retain price-sensitive customers, or a downgrade to keep users at a lower commitment level.  
  
_HubX is an app portfolio company that has been executing a**Web2App** or web funnels strategy and has already **saved $100,000+ in churn** with cancellation flows. _

[**Read the full story here**](https://www.paddle.com/customers/hubx-sells-mobile-apps-on-the-web-with-paddle)

### Strategic friction

Some developers are experimenting with the introduction of friction, in an effort to improve overall conversion efficacy.

Rather than rushing users immediately to external payments, these apps are introducing "strategic pauses" that actually increase final conversion rates. 

This involves adding intermediate steps that build user investment and trust before the payment transition.

This may take shape as a personalization screen, a progress indicator, or even a mini-assessments between the initial app experience and the external payment.

Users who complete these additional steps show significantly higher conversion rates and better long-term retention.

### **Audience-specific friction strategies**

Different user demographics respond to friction differently, requiring tailored approaches. 

Gaming audiences are accustomed to progression mechanics and respond well to "unlocking" payment options through engagement. 

Some games now require users to complete a tutorial or reach a certain level before presenting external payment options, resulting in higher-value customers.

Productivity app users prefer efficiency but appreciate customization. Strategic friction often involves plan configuration or workspace setup that makes the eventual purchase feel more valuable and personalized.

Health and fitness app users respond well to assessment-based friction, where additional screening questions actually increase their confidence in the app's ability to help them achieve their goals.

## Implementation strategy and rollout plan

Here's a recommended approach for implementing external payment methods in your app: 

### **Phase 1: Evaluation and Planning (1-3 days)**

  1. Assess your app's current conversion metrics to establish a baseline.
  2. Identify key metrics that could be improved through implementing external payments.
  3. Conduct a team brainstorming session to explore implementation options.
  4. Select[ the right payment solution.](https://www.paddle.com/in-app-purchase)
  5. Develop a testing strategy and identify user segments for experimentation.


### **Phase 2: Initial Implementation (4 - 6 days)**

  1. Build a simple initial implementation (button on paywall linking [to a web checkout](https://www.paddle.com/blog/web-checkout-tools-ios-apps)).
  2. Set up proper attribution tracking.
  3. Implement trust-building elements in the checkout experience.
  4. Launch A/B tests with a portion of your user base.


### **Phase 3: Optimization (Ongoing)**

  1. Analyze conversion data from initial tests.
  2. Experiment with different payment flows, discount strategies, and UX patterns.
  3. Expand successful approaches to larger user segments.
  4. Implement advanced cancellation flows and retention strategies.
  5. Continuously monitor attribution data and refine marketing strategies.


## Challenges to keep in mind

### **Infrastructure and operational considerations**

While this App2Web strategy offers compelling opportunities, developers should approach this transition with an air of caution.

The App Store handles several critical functions that many take for granted:

### **Chargeback disputes**

When customers dispute transactions, the App Store handles this if you purchase through Apple. However, using an alternative payment provider means developers must manage this themselves and respond with evidence and documentation for any disputed transactions.

Each chargeback requires formal responses with transaction records and proof of service delivery.

The process is time-consuming, expensive, and requires banking regulation expertise that most app teams lack.

### **Global payments management**

Supporting different payment methods across international markets requires significant infrastructure. Each region has preferred methods: PayPal dominates in Germany, while Alipay is essential in China. 

Developers must integrate multiple gateways, handle currency conversions, and optimize payment routing for higher acceptance rates.

### **Fraud prevention**

Protection against payment fraud becomes the developer's responsibility when selling on the web. Unlike app stores that handle fraud detection automatically, web payments require actively monitoring suspicious transactions. Apps face risks from stolen credit cards, account takeovers, and bot traffic, with potential financial losses and account termination.

### **Subscription management**

Managing subscriptions on the web requires building infrastructure for trial tracking, automatic renewals, proration calculations, and failed payment handling.

The complexity increases with coupon codes, multiple tiers, and regional pricing. Failed payment recovery alone requires sophisticated retry logic and customer communication workflows. Many apps lose significant revenue from expired cards without proper recovery systems.

### **Global tax compliance**

Managing international tax obligations introduces substantial complexity and requires ongoing management, especially as you scale. 

Tax compliance for digital products varies dramatically by jurisdiction. Each region has different registration thresholds, tax rates, filing frequencies, and documentation requirements. 

As apps grow internationally, developers must register in multiple jurisdictions, calculate correct rates, file returns, and remit payments on schedule. Penalties for non-compliance can be severe.

### The solution: Merchant of Record

As a [Merchant of Record (MoR)](https://mor.paddle.com/), Paddle handles all of these complexities just like the App Store does, but at a fraction of the cost. 

Paddle manages global payments infrastructure across 30+ currencies, handles all fraud protection and chargebacks, automates subscription management from trials to renewals, and takes complete legal responsibility for tax compliance in 100+ jurisdictions worldwide.

This gives you all the operational benefits of the App Store's backend infrastructure with lower fees, faster payouts, and complete control over your customer relationships and pricing strategies.

[**Learn more about Paddle for external payments**](https://www.paddle.com/in-app-purchase)

![](https://images.prismic.io/paddle/Zyos7q8jQArT0NuT_Paddle-MerchantofRecordmodel.jpg?auto=format%2Ccompress&fit=max&w=3840)

### **Attribution complexity**

It's important to keep in mind that an App2Web motion introduces new complexity to attribution models. 

Suddenly, you may have campaigns where users stay within the app, transition from app to web, or move from web to app, creating multiple attribution paths to track.

Mitigation strategies include:

  * Utilizing server-to-server events and APIs from attribution platforms
  * Running fewer channels initially to simplify attribution
  * Implementing custom attribution models
  * Conducting incremental testing to validate attribution approaches


### **User experience (UX) friction**

The potential for increased user friction when transitioning between app and web environments remains a significant concern. 

Developers who wait for others to implement first may benefit from reduced friction as users become familiar with these new payment patterns, but they also risk missing the early-mover advantage.

All roads lead back to experimentation.

As mentioned earlier, test and test again to find out how you can use friction to your own advantage and what your audience responds well to.

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)

Related[Case Study![](https://images.prismic.io/paddle/aCyMvidWJ-7kSWXS_paddle-billing-x-stoikk.jpg?auto=format%2Ccompress&rect=0%2C0%2C1200%2C628&w=1080&fit=max)No drop in conversions, launched in days: How Stoikk capitalized on the App Store ruling](/customers/stoikk-web-checkout-third-party-payments)

## Ready to rise to the opportunity?****

The opportunity to implement external payments from your app represents one of the most significant shifts in the mobile app ecosystem in recent years. 

While challenges exist, early data from companies like Stoikk suggest that well-executed implementations can maintain or even improve conversion rates while reaping the rewards of greater revenue.

The key to success lies in rapid experimentation, careful attention to user experience, and a focus on building trust throughout the payment process. 

App developers who move quickly and thoughtfully stand to gain a significant competitive advantage in the evolving landscape of mobile app monetization.