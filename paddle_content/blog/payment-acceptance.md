---
title: "Payment acceptance: the million-dollar metric most SaaS executives are missing"
description: "Our experience working with over 2,000 software companies migrating or launching on Paddle is very few SaaS executives are optimizing or are even aware of payment acceptance as an issue. This a deep dive guide to help you get back on track and retain the revenue you’ve already sold."
source: "blog/payment-acceptance.html"
---

# Payment acceptance: the million-dollar metric most SaaS executives are missing

Our experience working with over 6,000 software companies migrating or launching on Paddle is very few SaaS executives are optimizing or are even aware of payment acceptance as an issue. This is a deep dive guide to help you get back on track and retain the revenue you’ve already sold.

![](https://images.prismic.io/paddle/fc72f7e4-119a-4600-8eba-93485501a712_ed-fry.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Ed Fry](/resources/author/ed-fry)

Share

[](https://x.com/intent/tweet?text=Payment%20acceptance%3A%20The%20million-dollar%20metric%20most%20SaaS%20executives%20are%20missing%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-acceptance%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-acceptance)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-acceptance&title=Payment%20acceptance%3A%20The%20million-dollar%20metric%20most%20SaaS%20executives%20are%20missing&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

Your funnel has a hole in it.

Failed payments are the menace of selling anything online. Successful payment acceptance is dependent on the workflows and infrastructure underpinning how you take payments, and how you optimize for payment acceptance. Selling SaaS often means selling globally, which complicates matters. It's why online payment acceptance rates are significantly lower than buying something in-person.

Here at Paddle, we’ve dedicated engineering teams to optimizing payment acceptance for years. Their work has a significant lift on the hundreds of millions of dollars of ARR that flows through the Paddle platform.

And yet, our experience working with over 6,000 software companies migrating or launching on Paddle is **very few SaaS executives are optimizing or are even _aware_ of payment acceptance as an issue.**

We've created a deep dive guide to help you get back on track and retain the revenue you’ve already sold.

In this guide

  * [What is payment acceptance? ](#what-is-payment-acceptance)
  * [Why it likely hasn't been on your radar ](#why-you-don't-know-about-payment-acceptance)
  * [How to calculate payment acceptance ](#how-to-calculate)
  * [How banks talk to each other ](#how-banks-talk-to-each-other)
  * [8 reasons for low payment acceptance ](#8-reasons-for-low-payment-acceptance)
  * [Your business depends on payment acceptance ](#your-software-business-depends-on-payment-acceptance)
  * [The value of improving your payment acceptance ](#the-value-of-improving-payment-acceptance)


## What is payment acceptance?

In the simplest terms, payment acceptance is the proportion of payments that are successful out of the total number of payments that are attempted. In credit card language, this is often called the “authorization rate”. The inverse metric is your "failed payment rate".

## Why payment acceptance is your most important revenue-generating workflow that you probably know nothing about

Your revenue streams and income are built around a small number of workflows and processes. If you’re in a B2C or B2B, self-serve or sales-assisted model, you’ll probably have some or all of these revenue-generating workflows active.

  * Signup funnels and onboarding (optimizing conversion rate)
  * Lead scoring and routing (optimizing qualification & opportunity creation rate)
  * Subscription billing (optimizing lifetime value)


There’s an  _enormous_ volume of literature and understanding in the SaaS space around every one of these.

Payment acceptance affects everyone. Even with the best signup funnel, lead scoring, and subscription billing workflows imaginable, low payment acceptance will dramatically decrease your revenue. Successful selling does not guarantee money in the bank.

But unlike other industries dependent on online payments, payment acceptance is not a common metric discussed in SaaS. Often, we outsource all our payment processing and all the day-to-day management and optimization to third-party providers.

And so we don’t see “payment acceptance” in any of the common [SaaS metrics](https://www.paddle.com/glossary/saas-metrics) discussions like [LTV:CAC ratio](https://www.paddle.com/resources/cac-ltv-ratio), CAC payback, quick ratios, and AARRR “Pirate Metrics”.

In this comprehensive guide, we’re going to unpack:

  * What payment acceptance means
  * How to think about payment acceptance (so you can optimize it) meaningfully
  * And take a tour through the underlying infrastructure that’s working on your behalf


## How to calculate payment acceptance

You can calculate this by pulling data from your payment processor (most tools allow you to export payment data as a CSV for all payment attempts - failed and successful).

![](https://images.prismic.io/paddle/6e4f5f95-8d82-4590-88c4-4afbfac41872_payment-acceptance-equation.png?auto=format%2Ccompress&fit=max&w=1920)

**But never ever look at payment acceptance in aggregate.** It’s too generic to be accurate or meaningful, particularly in a subscription business.

You need to account for retried payments (say, due to lack of funds or incorrect card details), failed payments over different billing periods (like annual subscriptions paid by card vs. monthly), different payment methods (where credit cards aren’t a direct source of funds but a bank wire transfer is), country, and so on.

_Maybe this is why it isn’t a widely-used metric?_ 😏

You’re right!

From your payment processor, you should be able to extract data around payment attempts. For instance, with Stripe you can export all payments (including failed payments).

With that data in hand, here are five useful ways to segment payment acceptance in a meaningful way.

  1. **Unique payment acceptance** Count based on checkout attempts vs. individual payment attempts. Sometimes called “net” payment acceptance.  

  2. **Payment acceptance by payment type** Comparing payments through “checkout”, automated subscription payments, and updating card payments. This is especially important for SaaS businesses.  

  3. **Payment acceptance by billing cycle** How do annual subscription payments compare to monthly or 1-time payments.  

  4. **Payment acceptance by payment method** Comparing payment methods like PayPal, direct debit, and card.  

  5. **Payment acceptance by country** Comparing payment acceptance rates across different countries.


**Key Takeaway: “Raw” payment acceptance isn’t a helpful metric alone** You need to understand it in the context of successful payments, checkout vs. recurring, countries, payment methods, and so on. With the right metric to optimize, you need to understand the mechanics of what you’re optimizing. So let’s dig into the banking & finance infrastructure behind all of our businesses.

## How banks talk to each other

Whatever the payment method being used, there’s still a common pattern to how money moves from your customer’s bank account to your bank account.

Payments need three things:

  1. Funds available to pay (duh..)
  2. Valid request sent over shared payment networks
  3. Accounts to transfer money between


So let’s say a customer has the money 😉(it’s a very boring post otherwise…)

Whether it’s via credit card, wire transfer, or sending a check, it all starts by sending a message with all the information needed for the payment over a shared network.

  * Checks are a **physical message**(the network is the postal mail to a bank branch)
  * Wire transfers use **networks**(like Fedwire, SEPA, and SWIFT - more on those later... )
  * Cards run through your “acquiring bank” via **card schemes**(like Visa & MasterCard) to the customer’s “issuing bank”


The request for payment is either authorized or declined. Authorization is an agreement by banks to transfer the money.

Clearing and settlement come last. Clearing is the updating of bank account details and settlement is the actual transfer of money.

For clearing and settlement to happen, banks need to transfer funds between the accounts they hold with each other. These reciprocal accounts in other banks are called **“correspondent bank accounts”**.

If they don’t have corresponding banking relationships, they need to transfer funds via another bank(s) who do - in the context of payments, this is sometimes called a **“payment chain”**. It becomes important with optimizing several parts of payments you’ll see later...

**Key Takeaway: Think of the 1-2-3 model for payments** All payments have these three parts in common - funds available, message over a network, and the transfer between accounts. This is helpful for understanding and improving payment acceptance.

## Eight reasons for low payment acceptance 

### 1\. Lack of funds from the payment method

“No funds” is the second-highest cause of payment failure.

Over millions of payment attempts across the Paddle platform, we generally see 19% of all failed payment attempts are caused by the lack of funds (most payment processors return this in their decline reasons).

Card payments (particularly credit & pre-paid cards) are most common to be declined for this reason since they have credit or spend limits imposed. These limits are usually lower than a real source of funds.

How do you capture this lost revenue?

  1. Retry payments (if on subscription)
  2. Offer alternative payment methods


**Retrying payments is critical to raising your overall rates.** Most subscription billing tools will offer a time-based follow-up. More sophisticated tools will learn patterns for smart retries, like the dates in a country that payroll is done. [We see this reduces revenue churn by around 10%.](https://www.paddle.com/blog/reduce-churn/#strategy-4)

One key indicator of how effectively your routing and retry logic is working is if payment acceptance is high, but there are also lots of payment attempts the delta between the number of payment attempts and the number of successful payments.

A big difference in performance indicates lots of retries are being attempted on average to maximize your [revenue performance](https://www.paddle.com/resources/revenue-performance). At Paddle, we average 107 payment attempts per 100 successful transactions to ensure the highest payment acceptance rates.

Alternative payment methods can connect to a direct source of funds. Digital wallets like PayPal hold a balance and can draw from multiple other sources (like credit cards and bank accounts). Bank accounts themselves act as a direct source of funds.

At Paddle, we see card payments have more than 2x the proportion of failed payments compared with sources like PayPal and wire transfer where they’re far less likely to decline due to “lack of funds”. That’s why we’re excited about digital wallets, particularly those that support subscriptions and support higher-value B2B transactions.

**Key Takeaway: You need a strategy for “no funds” declines** As the second-highest decline reason, you need to have retries and offer alternative payment methods to capture that revenue.

### 2\. “Card not present” transactions

Online card payments are all “card not present” or **CNP transactions**. Since the card isn’t present, it’s easier for fraudsters to try to use a card to buy something without revealing their identity. This is why payment acceptance is significantly lower for CNP than in-person “card present” transactions.

This is especially problematic for [subscription renewals](https://www.paddle.com/resources/subscription-renewal) when the card is not present AND the customer is not present, so they can’t react to a decline on the screen in front of them. Even with notification later, they’re likely to still have access to the software. There’s significantly less communication and motive to take action  _immediately._

Subscription renewal payments actions are “merchant initiated transactions”, unlike checkout or updating payment details. The payment acceptance here is lower, even with tokenization and vaulting of the card (so you are authorized to charge again in the future).

Tokenization and payment routing can fall in conflict with each other. To route and retry payments, you need to have authorization. If that token is tied to a payment processor, you need to either:

  1. Get authorization again (which is very disruptive to your customer’s experience 😒)  
  
or...  

  2. Manage routing of payments through a payment switch (at additional cost) or use a platform with a payment routing managed for you (like Paddle).(Rarely does this make sense to build yourself since you would take on responsibility for PCI compliance - [this is no joke. ](https://www.pcisecuritystandards.org/pci_security/how))


Across all payment attempts at Paddle, we see the**raw payment acceptance of renewal payments is lower than that of checkout or updating payment details**.

This is why it’s important to have retry logic built into your payments and billing system. Not only does this help catch your lack of funds, but it helps to [reduce involuntary churn ](https://www.paddle.com/blog/reduce-churn/#strategy-4)after a payment has failed.

**Key Takeaway: Payment acceptance for subscription renewals is lower** __ You need to have retry logic with the card tokens on file, or payment routing to try alternative source to maximize payment acceptance with subscriptions.

### 3\. Wrong, missing, or expired information

Incorrect and missing information stops payment messages from sending in the first place.

  * Wrong card numbers
  * Incorrect billing address
  * Missing country


Any of these (and more) can cause the initial payment message to fail.

You need to have [card validation in your checkout forms ](https://medium.com/hootsuite-engineering/a-comprehensive-guide-to-validating-and-formatting-credit-cards-b9fa63ec7863)so customers can clearly send the right data through. These include attributes like credit card number length (16 characters), validity ([ check out the Luhn algorithm ](https://www.creditcardvalidator.org/articles/luhn-algorithm)\- it works for most card types), and CVV (3 characters, 4 for American Express).

You should also design visual cues into your checkout to indicate the formatting required. At Paddle, we offer this via our plug-and-play overlay checkout.

![](https://images.prismic.io/paddle/3c41fcde-5fb0-4759-bcf6-8e4cd281af74_tailwind-labs-checkout.png?auto=format%2Ccompress&fit=max&w=3840)

If you’re building your own “inline” checkout forms, don’t forget to build credit card validation into the form design and data submission.

**Expired, deactivated & canceled cards reduce payment acceptance too.**

Unlike other payments, you’ll notice credit cards don’t last forever. Different laws and regulations, as well as fraud mitigation from issuing banks means that cards are required to have an expiry date.

With an average 36 month lifespan, you might see 2-3% of your cards on file expire each month before cancellations and deactivations.

Of course, payment acceptance drops when cards on file can’t be charged. 🤷

This particularly impacts annual subscriptions paid by card. Offering annual upfront is a SaaS best practice for driving cash flow, but it needs to be paired with a payment acceptance strategy to keep customers on when their renewals come up.

In practice, this requires updating card details by either:

  1. Prompting the buyer to update their details
  2. Automatically updating card details via banks


Firstly, prompting buyers to update card details can lead to them reconsidering their purchase outside of the context of the product - this can [increase the number of customers opting to cancel and actively churning](https://www.paddle.com/blog/reduce-churn).

It’s important to test this and explore in-app notifications or live chat vs. emailing people out of context.

The second option is automatic. Card schemes maintain “account updaters” like [Visa Account Updater ](https://developer.visa.com/capabilities/vau)and [MasterCard Automatic Billing Updater ](https://globalrisk.mastercard.com/online_resource/automatic-billing-updater)which sync updates to card credentials on file and extend the life of that account so recurring payments can still be charged.

The challenge is this will only represent a small portion of cards - you can expect between 2.5-5% of cards run through a card updater service to be updated on a regular basis or when the payment is processed (depending on your provider).

Most payment processors and payment switches will offer service around this, though some may pass on (and maybe mark up) the charges from card schemes for running the lookup.

### 4\. Fraud triggers

Fraud is a massive problem for online payments.

In 2020, [online payments are worth about $2.93 trillion dollars ](https://www.statista.com/outlook/296/100/digital-payments/worldwide)with over [$17 billion dollar lost to fraud ](https://www.juniperresearch.com/document-library/white-papers/fighting-online-payment-fraud-2020)\- about 0.6% of transaction value.

(Fun fact: $17 billion is the [same amount of money Netflix will spend on new content in 2020 ](https://variety.com/2020/digital/news/netflix-2020-content-spending-17-billion-1203469237). 😮 See, if we didn’t have fraud… we’d have higher payment acceptance AND maybe another Netflix!)

**Whilst credit card schemes like Visa and MasterCard can help with identifying fraud, it is banks who stand to lose money here** \- particularly issuing banks who take the hit for credit cards (this is one of the reasons their fee structures are so much higher than other payment methods) since it is them, not the customer that is out of pocket.

Losing money isn’t just a profit-and-loss problem for banks - it also impacts liquidity and how money can move between accounts. Since that’s the lifeblood of banking, banks are very intolerant to track records of fraud, [chargebacks](/resources/chargebacks), and even high refund rates. 

To minimize their losses, **banks are very heavy-handed in how they decline authorization where they suspect fraud**. This disproportionately impacts smaller, lower volume sellers in “card not present” categories.

The volume of “false declines” (which genuine online payments are declined) dwarfs the actual volume of fraudulent payments - [this report estimates false declines will reach $443 billion dollars per year by 2021 ](https://aitegroup.com/report/e-commerce-conundrum-balancing-false-declines-and-fraud-prevention)and continue to grow. That makes false declines about 15% of all online payment attempts.

It also indicates that for every $1 in fraudulent online payments, $25 of genuine online payments are falsely declined. This 25X multiplier illustrates just how risk averse banks are - they would rather forgo the value of $25 worth of transactions than risk losing $1 to fraud.

🚫 TL;DR: when banks are in doubt, they decline.

**This is not how card schemes would have it.** The public rules from card schemes all have an “honor all cards” provision - you can’t arbitrarily discriminate between card types (with a small number of exceptions that aren’t relevant to software businesses).

[Mastercard’s version ](https://www.mastercard.us/content/dam/mccom/global/documents/mastercard-rules.pdf)states this require this:

“A Merchant must honor all valid Cards without discrimination when properly presented for payment. A Merchant must maintain a policy that does not discriminate among customers seeking to make purchases with a Card.”

[Visa’s version is very similar ](https://www.visa.co.uk/dam/VCOM/download/about-visa/visa-rules-public.pdf)and goes on:

“A Merchant may also consider whether present circumstances create undue risk (for example: if the sale involves high-value electronics but the Card signature panel is not signed, and the Cardholder does not have any other identification).”

But it’s still up to the bank to decide whether a transaction looks fraudulent.

**🕵️ Two factors behind fraud triggers**

The fine details of how banks assess fraud, but the core principles are common to lots of problems from fraud to online product reviews - [this video dives gives a brilliant explanation of the latter ](https://www.youtube.com/watch?v=8idr1WZ1A7Q).

There are two things I can evaluate to determine

  * How many transactions have I seen?
  * What’s the expected success rate?


One way to think about this is what might the impact be of the next two observations - a “rule of succession” (a statistical technique from the 18th century).

If it was a 50:50 coin toss between being a fraudulent and genuine transaction, what would the impact on my expected outcome of adding one success and one failure be?

If I’ve a very small number past observations (or none at all!), then the impact would be substantially different. If the number was larger, it may have less impact.

(Of course, real fraud algos are much more complex than this, but…)

**This helps to illustrate two drivers for reducing false declines in selling online software** \- you need to have low fraud and chargeback rates, but you also need a high volume to assure banks that you’re a trusted merchant.

**How “false declines”** 💥**impacts software businesses**

Software doesn’t have specific provisions made for high-value, cross-border transactions like airlines or hotels. Instead, card schemes have a few codes to help classify transactions for fraud, transaction fees, as well as tax purposes:

  * **Merchant Category Code (MCC)** \- a four-digit code to classify a merchant by what goods or services it sells. This is a common standard under [ISO 18245](https://www.iso.org/standard/33365.html).
  * **Transaction Category Codes (TCC)** \- specific to card schemes like Mastercard for classifying how transactions occur (like ‘card not present’)


You can’t spoof MCC’s and also build a sustainable business. MCC’s were introduced by the IRS in 2004 for sales tax reasons. Tax authorities can and will come after you and your company for tax evasion (since some jurisdictions have different standards for different types of products).

There’s clear legislation & guidance from tax authorities that outright tax evasion carries severe penalties and prison sentences in most countries, including countries you don’t physically operate in.

(Sales tax in software is complicated too. [Our CFO has a video & guide here ](https://www.paddle.com/blog/global-sales-tax-faqs)).

Since tax authorities introduced MCC’s, card schemes and banks also use them to:

  * Determine the risk profile of a merchant (i.e. high-risk categories like gambling)
  * Block certain merchants from using a card scheme
  * Calculate credit card rewards based on categories


This means your software business will be judged according to their data and algorithmic biases within your category. There’s no reasonable way to evade this.

**👀 What does this mean for SaaS businesses?**

**SaaS and 1-time downloadable software falls under the MCC code 5817** and involve “card not present” transactions. [MasterCard’s Quick Reference PDF explains the category ](https://www.mastercard.us/content/dam/mccom/en-us/documents/rules/quick-reference-booklet-merchant-edition.pdf):

“Merchants that sell prewritten software applications made available to a cardholder via remote access (for example, a hosted server) or download. Such applications include, but are not limited to, accounting or financial programs, office suites, data management resources, image organizers, media players, and animation development tools.”

It’s important to note that **this does not discriminate between B2B and B2C purchases**. At Paddle, we see chargeback rates on software sellers migrating from other platforms up to 20X as high as our seller average before any [chargeback reduction programs ](https://www.paddle.com/features/chargeback-protection)are in place.

“Riskier” categories tend to be B2C transactions, high volume, and aren’t constrained by geography (whereas B2B software transactions tend to concentrate in geographies with higher GDP per capita like Europe and North America where people are more expensive.).

In B2B software, you’re charging a relatively low volume of high-value payments that sometimes cross-borders too. Even with positive signals like a legitimate legal entity, this sort of transaction shares a similar fingerprint to higher-risk software sellers.

To tackle this, you can adopt a:

  1. **Passive strategy** \- build up volumes and improve payment acceptance over time (accepting this won’t be a business driver)
  2. **Active strategy** \- seek out fraud tooling and proactively optimize for reducing chargebacks. Some of the best-in-class fraud protection tools start at around $30,000 per year (including tooling we use at Paddle).


In comparison, Paddle acts as a reseller for thousands of software businesses. We concentrate hundreds of millions of dollars worth of revenue through one MCC, plus a consistently low chargeback rate across our transactions (due to our [fraud protection ](https://www.paddle.com/features/credit-card-fraud-protection), [chargeback prevention ](https://www.paddle.com/features/chargeback-protection), account management, and [subscription support ](https://www.paddle.com/platform/managed-support)).

**Key Takeaway: SaaS businesses need volumes of payments to combat fraud signals** __ Using a reseller means your business leverages their volumes and “reputation” for minimizing false declines and maximizing payment acceptance.

### 5\. Payment requests don’t share the same format

Remember, what matters is having a good relationship between banks.

Just like spoken and written languages, banks speak different “languages” to communicate between them. These tend to center around common standards for communication like shipping containers, plug socket sizes, W3C standards for the world wide web, and so on..

**There’s just one problem. - standards aren’t shared across all banks. 😩**

There hasn’t been an equivalent of what W3C does for the internet in the banking space. But that is slowly beginning to change.

There’s an enormous move in the financial sector to enable common standards for financial transactions (including payments) - called [ISO 20022 ](https://www.iso20022.org).

(ISO stands for [“International Organization for Standardization”](https://www.iso.org/home.html). They help create & evolve common standards).

In [ISO 20022 for Dummies ](https://www.swift.com/sites/default/files/resources/swift_iso20022s_standards.pdf)(don’t recommend the audio book… 😳), there's an explainer as to how creating a new standard for payments will benefit all parties involved.

“ISO 20022 messages will lead to higher end-to-end STP rates, with fewer false positives arising from poor-quality risk-bearing information in payments-related exchanges."

(They say it’s for dummies, but what a mouthful…)

Let’s unpack that…

STP is **“straight-through processing”** \- the banking industry term for automated transactions. Almost all modern transactions from trades to credit card transactions are STP and run through physical network infrastructure ([similar to the web](https://builtvisible.com/messages-in-the-deep)) - except for the goblins at Gringots.

**“Fewer false positives”** means banks are less likely to mark a genuine transaction as fraudulent because they have more **“risk-bearing information”**. In the absence of information or good quality information, a bank will err on the side of caution to avoid being liable for potential loss -  _remember, $25 in payments are declined for every $1 in real fraud._

ISO 20022 messages will carry more data and share a common language (syntax & semantics) and so issuing banks have the information they need to determine fraud on the merits of the data.

Starting in November 2021, most core banking systems are mapping their services and migrating to ISO 20022 standards for payments - over 10,000 banks worldwide.

But this process is incredibly complicated (therefore expensive) and impacts most of how banks and interbank networks (like SWIFT, Fedwift, SEPA, ACH, CHAPS) will communicate - see all that in red in [this paper on ISO 20022 migration from Deutsch Bank ](https://www.cib.db.com/docs_new/UltimateGuide-EN-Top.pdf).

![](https://images.prismic.io/paddle/813008a2-c9e1-4e23-951c-271c33dfc88d_iso-20022-migration-impact.png?auto=format%2Ccompress&fit=max&w=3840)

It’s also important that 10,000 banks is only a fraction of the banks worldwide.

  * IBAN.com (the organization behind IBAN - the most common identifier for banks) has [over 330,000 individual banks and branches across 75 IBAN-participating countries worldwide](https://www.iban.com/our-data).  

  * SWIFT network (“Society for Worldwide Interbank Financial Telecommunication”) - which manages the messaging part of transactions between over 10,000 banks in over 200 countries.  
  
SWIFT issues banks with a Business Identifier Code (BIC) which are another form of routing transactions under [ISO 9362 ](https://www.iso.org/standard/60390.html). BIC codes are needed to connect to the SWIFT network - but less than 40% of the banks with a BIC code are connected to the SWIFT network.  

  * Within that, there are at least 1,500 banks that issue credit cards (often on behalf of other banks’ customers). Whilst it’s likely that issuing banks are larger, connected to SWIFT, and are adopting ISO 20022, it is the acquiring bank that sends the first message - including the message the issuing bank evaluates for fraud.


10,000 of 330,000 banks (around 3%) will have a strong incentive to move to ISO 20022.

In the meantime, almost all card transactions today follow another standard established in the 80’s - [ISO 8583](https://medium.com/plain-and-simple-series/all-things-tech-beautiful-iso-8583-an-introduction-plain-and-simple-21eb62455b28).

**Remember, standards are not regulations. ISO are not lawmakers.** So the [debates rage on ](https://www.linkedin.com/pulse/iso-8583-vs-20022-cards-mandatory-migration-required-yet-anzellotti)about migrating given the huge sunk costs and interdependency on other banks migrating over too (or migrating all to ISO 8583!).

So adoption is sloooow. Thousands of banks with incredibly complicated, incredibly expensive changes to migrate where no one gains significantly from being an early adopter. It makes software giants like Oracle, SAP, IBM, and Microsoft look as agile as hummingbirds…

(And just to  _really trigger techies folks_ , ISO 20022 is based on XML… )

**👀 What does all this mean for SaaS businesses?**

You can’t count on running your payments through a single provider for the coming 5-10 years. It’s too messy out there...

Until standards converge, you will experience declines from the failure of data transfer (like truncation) and loss of risk-bearing information in transit. This leads to banks falsely declining payments.

Instead, **you need to use an infrastructure that retries and resends requests for authorization through several payment routes**. The best payments infrastructure runs payment routing intelligently through different processors and banks based on historical data - machine learning is a powerful tool for optimizing here.

To do this, you need to choose the depth you want to build yourself -

**If you’re a global e-Commerce or payments giant** , you might build or integrate multiple payment processors with a payment switch to route and retry payments through different banks across the world. You might take on PCI compliance yourself too. You will have at least one full engineering team dedicated to payments optimization and orchestration.

**But if you’re a software company** , it’s more likely your engineering resources are invested in product development than payments optimization. That’s why it’s common to run through a payments facilitator who does  _some_ of this on your behalf.

But this limits you to a single set of relationships and network. You miss a lot of opportunities to optimize, which is especially effective when you deal with cross-border fees…

**Key Takeaway: Retrying through different routes improves payment acceptance** __ If you’re using only a single payment processor, you may only have “one shot” at a payment going through.

### 6\. Genuine cross-border “foreign” transactions get easily declined

Cross-border payments expose many of the challenges with how banks talk to each other.

**Firstly, cross-border transactions will have longer payment chains** which increases the chance of error due to different messaging standards and decline.

Remember, banks need to hold “correspondent accounts” with each other to transfer money between them. This takes money or “liquidity” to maintain (so you can payout to accounts when requests to settle come), so banks will only maintain correspondent accounts where they have enough volume of transactions to exchange between them.

Increasing regulations after the 2008 crisis have driven the trend in banking towards consolidation. This is particularly true with international payments - it’s hard enough to meet new standards and regulations in your own country, let alone hundreds of others.

This paper by the Bank for International Settlements shows that whilst cross-border transaction volume is booming, [correspondent banking relationships and even country-to-country connections are on the decline ](https://www.bis.org/publ/qtrpdf/r_qt2003g.pdf)across the SWIFT network (mentioned before).

![](https://images.prismic.io/paddle/9c8566ad-8311-4075-bf79-85fbd212dde4_swift-correspondent-banking-decline.png?auto=format%2Ccompress&fit=max&w=3840)

If you look at this on a country level, the picture looks grim - particularly in North America and Europe which dominate B2B SaaS volumes.

![](https://images.prismic.io/paddle/82ea5f78-8441-46cb-96b5-c3c8838e4f33_swift-active-correspondent-global-trends.png?auto=format%2Ccompress&fit=max&w=3840)

This means payments get routed through middlemen - larger banks with more liquidity that can hold correspondent accounts with banks across the world.

Each of these middlemen banks adds fees (what you’ll see as **“cross-border fees”** or **“international payments”** in most payment processors) as well as the chance for errors in data and transactions being flagged for fraud.

**Secondly,[foreign banks are unlikely to have existing relationships ](https://www.americanexpress.com/us/foreign-exchange/articles/decline-correspondent-banking-solutions). **With many correspondent banks in between, it’s much less likely that international acquiring banks have relationships with your customer’s bank for your company (or “merchant ID”) and category.

From the fraud lens, it becomes much more challenging for the issuing bank to determine whether a transaction is genuine without definitely depending on.

A merchant bank in middle America is unlikely to hold relationships with an issuing bank in Brazil, the UK, or China. Instead, they would have to route through acquiring banks like Bank of America (US), Barclaycard (UK), or Cielo (Brazil).

**There’s also simply the connectivity issue - American Express highlights this well given their unique model.** American Express operates as both a card scheme (like Visa & MasterCard) but also an issuing bank (AMEX issue their own card accounts to customers). It’s on them to build up “merchant acceptance” and acquiring networks.

In their [2019 investor’s report ](https://ir.americanexpress.com/#parentHorizontalTab3), American Express shared their “parity merchant acceptance” in the US with 99% merchant coverage, but also their progress with international acceptance.

“We also made good progress increasing merchant coverage in international markets where our Card Members live, work and travel to the most, adding more than 2 million merchant locations in 2019. This remains a focus for us in 2020.”

For comparison, [Visa have over 46 million merchant locations worldwide ](https://www.visa.co.uk/dam/VCOM/download/corporate/media/visanet-technology/aboutvisafactsheet.pdf).

At Paddle, we operate to only resell software and at very high volumes - just this past week we’ve sold across 228 countries across hundreds of thousands of transactions. We’ve a far higher likelihood of engaging with different banks around the world on a regular basis.

**Finally, there’s genuine fraud risk with foreign transactions.** We’ve already discussed high-value, “card not present” trials in the software category being a risk - foreign transactions adds more intermediaries, remove trusted correspondent relationships, and increase that risk that the issuing bank doesn’t get paid out.

There are also more chances for fraud signals to look fishy. Let’s look at different types of country data:

  * Issuing bank’s country - also the country of the customer’s card
  * IP address of the checkout (which should match the customer’s card)
  * Email address of the checkout should match the countries card
  * Country of the merchant
  * Acquiring bank’s country


Imagine a $200 software purchase on an Irish-issued card (and customer) to an Australian merchant via a US acquiring bank from a Canadian IP address. To the Irish issuing bank assessing that request, does this all line up as a legit transaction? 🤔

This is very easy to spot. For instance, the first numbers on your credit card are designed to [identify the bank and country that issued it ](https://www.creditcardvalidator.org)\- try it out in [this interactive tool ](https://binlist.net)(don’t worry, it only asks for the first bit!)

👀 **What can you do about it?**

Selling internationally is all about banking locally.

The single most effective strategy is using local acquiring banks. These are the banks working for you that request funds via the card scheme from the issuing banks.

Remember, it’s not about card schemes (their terms say “honor all cards”) but the relationships between banks.

Local acquirers are far more likely to have relationships with issuing banks in the same country - they may even be the same bank! ChasePaymentech is one of the largest acquiring banks & merchant services, whilst Chase is also the largest issuing bank in the US.

To route payments to local acquirers, you need to connect your payment switch (routing logic), payment processor (for the transaction), and acquiring bank together.

When we A/B tested local acquiring in the US at Paddle, we saw a **20% increase in checkout payment completions, and a 3% increase in subscription payments completions**(that 3% improvement that can compound each month).

This is just for the United States - a well-connected economy with established banking.

This isn't just a Paddle fluke - it really works.

Few case studies truly exist around authorization rates and payment acceptance through local acquiring, although you can find some -[ Wix moved from 30% to 85% payment acceptance in Brazil](https://www.zooz.com/post/how-do-i-go-global-life-of-a-head-of-payments-chapter-3) with local acquiring relationships. 📈

“The results were amazing! An 85% success rate on initial purchases (everyone told us not to expect more than 70%-75%), and the second country (after the U.S) in the number of premium plans sold. But remember -**** this process took us nearly a year to accomplish.”

👀 **How do you set up local acquirers?**

In most countries, banks will require you to have a local business entity before opening any account with them.

For software companies, setting up business entities all over the world typically isn’t a priority until later stage or if establishing field offices. This burdens the business with admin, tax, employment, and financial red tape.

The red tape continues with establishing the relationship with each acquiring bank - companies who have done this report it taking almost a year to get set up for processing payments (including refunds, chargebacks, and any local regulations), and then several months with volumes before payment acceptance started to rise whilst the banks are still _“getting to know you”_.

**Then you need to repeat this for every geographic market you wish to optimize. 😰**

Building this all yourself is not the only option.

Similar to how many remote or global software companies start with contractors or agencies acting as the “employer of record” (so they can just “turn on” talent and be compliant without getting tangled in the regulations themselves) you can go-to-market globally through a reseller under a [“merchant of record” ](https://www.paddle.com/features/merchant-of-record)model that manages and optimizes payments on your behalf.

Paddle operates under this model so thousands of software sellers can leverage our platform, infrastructure, tax compliance, and historical relationships to optimize for faster growth in local markets.

**Key Takeaway: Selling internationally is about banking locally** Use local acquiring banks who have local banking relationships to dramatically increase your payment acceptance in foreign markets.

### 7\. Currency conversion

Even if banking relationships exist, there is another layer of complexity when you introduce foreign currencies.

**All the challenges with cross-border payments are made worse by selling in a single currency.**

  1. You force a **longer payment chain**(fewer banks will hold correspondent accounts in different currencies)
  2. You are much more likely to **route around existing relationships**
  3. You add more **fraud triggers**


From earlier, we’ve established the trend for international banking relationships is on the decline due to higher costs, risks, and regulations. This concentrates foreign transactions to route through larger banks.

With foreign currencies, smaller banks lack the liquidity to hold funds in multiple currencies to enable exchange. It’s much more likely payment chains become longer and relationships between banks don’t exist.

Managing accounts in many different currencies - **“treasury management”** \- also exposes that bank to the daily rises & falls in foreign exchange value.

(Remember, only 0.6% of online payments are truly fraudulent, but banks are willing to decline 25x as many transactions to minimize their downside. Banks are very risk-averse in the context of payments and act disproportionately to compensate.)

This translates into much higher costs which get passed on in foreign exchange fees, but also justify the premium in the market. With fewer banks able to carry the liquidity needed for foreign exchange, there’s less competition to drive down these prices too.

Foreign exchange fees get passed on from issuing banks to the buyer or seller (depending on who is “converting”).

**How do local currencies impact payment acceptance?**

We also see higher  _conversions -_ i.e. more attempted payments - by introducing local currencies.

At Paddle, sellers can turn on and reprice products in dozens of currencies in a couple of clicks.

We see 🇨🇦 Canadian (CAD), 🇦🇺 Australian (AUD), and 🇳🇿 New Zealand (NZD) dollars have 1-2% higher payment acceptance in their home markets, but some markets like 🇯🇵 Japan, 🇰🇷 Korea, and 🇮🇳 India see 5-11% higher payment acceptance rates with local currencies.

**Local currencies shorten payment chains,** which reduces the chance of errors with data and increases the chance of acquiring and issuing banks holding correspondent accounts with each other. They don’t need to route through a larger bank for currency conversion. 

What’s clear from our seller data:

  * **In Asian markets payment acceptance benefits significantly just from local currencies** : Outside of China, most countries trade internationally with their own currency. South Korean Won and Japanese Yen are particularly effective where credit cards dominate local online payments and there are [lower levels of local credit card fraud ](https://www.jpmorgan.com/merchant-services/insights/reports/japan).  

  * **The US Dollar is dominant.** For companies outside of the US, introducing the dollar is a vital step to improving payment acceptance. This enables you to leverage the US banking infrastructure without routing through conversions.(Note: USD has 7% lower relative payment acceptance globally than within the United States).  

  * **In Latin America, currencies alone are not enough**. Local acquiring, local payment methods, and the regulations around it are larger blockers to connecting with customers' banks. Currencies here are often restricted and connect be bought and sold in foreign exchange.


There are a few challenges with offering additional currencies.

**Firstly, “piecemeal” payment stacks don’t handle foreign currencies very well**. Individual payment processors + subscription billing tools + SaaS metrics + invoicing tools + tax compliance tools become complicated with values denominated in different currencies.

For instance, most subscription tools require individual products for each currency that need to be re-integrated with all your other systems. Reporting depends on currency conversion (but which rate do you take?).

[Sales tax becomes even more complicated ](/blog/saas-sales-tax-state-wide-and-international)if single tax jurisdictions are served by multiple currencies via multiple tools (like invoiced wire transfers in USD but local card payments in GBP).

**Secondly, the foreign exchange fees introduced by payment processors.** Unless your payout currency is the same as the currency you charge in (SaaS-friendly banks like [SVB let you hold balances in multiple currencies ](https://www.svb.com/products/foreign-exchange/global-payments)), most providers will pass a marked-up currency conversion fee.

Even with this (usually between 1-3% depending on the currency and your payment processor), you ought to find yourself with a net gain across:

  * Higher conversions
  * Higher payment acceptance
  * Localized pricing


The way around this is to set up individual payment processors for each core currency and then run payouts into a bank that can take multiple currencies (or doesn’t charge you as much to convert).

**The challenge with both of these approaches is you end up wrangling lots of payment processors together** with routing payments upstream (including follow up support & chargeback requests) as well as unifying payment data to reconcile downstream across subscriptions billing, access management, sales tax, [revenue recognition](/resources/revenue-recognition-examples), and so on.

[Paddle manages this in a different way](https://www.paddle.com/features/payment-processing) \- by operating as a reseller you can turn on currencies and configure pricing in a few clicks then run through all our existing infrastructure. Paddle reconciles and converts payments into your payout currency so you get a unified stream of data and revenue.

**Key Takeaway: Use local currencies to improve local payment acceptance** … as well as improving conversions, and the ability to adjust pricing to local markets.

### 8\. Regulations and geopolitics

Ah, the final piece that no amount of routing, retries, local acquirers and currencies can save you from but can have a MASSIVE impact on payment acceptance.

🇪🇺 In Europe, Strong Customer Authentication (SCA) came into force in September last year under EU’s Revised Directive on Payment Services (PSD2). Banks can now challenge for SCA during “card not present” transactions (like online payments) and decline if it isn’t approved - Mike’s post goes into more details about [what SaaS businesses need to do to be compliant ](https://www.paddle.com/blog/psd2-get-compliant), particularly to preserve their recurring payments within Europe.

🇧🇷 In Brazil, there are a number of challenges to payments coming from international sellers. Cards are the most popular payment method, but most cards are national cards and cannot be charged internationally. Regulations also [tax cards at 6.38% for foreign transactions (to encourage domestic commerce) ](https://taxinsights.ey.com/archive/archive-news/brazil-decree-81752013-iof-increased-6-38-foreign-exchange-transactions.aspx). Local regulations restrict the movement of local Reals (BRL) out of the country. Brazil also sees some of the [highest levels of “card not present” fraud ](https://www.jpmorgan.com/merchant-services/insights/reports/brazil).

🇮🇷 In Iran, international sanctions against the country effectively cut it off from payments (Paddle’s payment acceptance rate in Iran is 0%). SWIFT, who connect international banks and are organized to be politically ‘neutral’, [wound up choosing to comply with the US sanctions ](https://www.ft.com/content/8f16f8aa-e104-11e8-8e70-5e22a430c1ad)undermining the EU’s efforts to maintain trade under the previous deal - [this led to the formation of INSTEX ](https://en.wikipedia.org/wiki/Instrument_in_Support_of_Trade_Exchanges)to provide an alternative. Iran is all but cut off from the rest of the financial world and what card payments there are tend to be via [pre-paid cards (which have a market of their own)](https://financialtribune.com/articles/economy-business-and-markets/59428/the-curious-case-of-prepaid-credit-cards-in-iran).

**What does this mean for SaaS businesses?**

As a business, you need to be aware and able to respond to laws and regulations affecting payments ([like sales tax](https://www.paddle.com/blog/global-sales-taxes-for-software-companies-what-you-need-to-know-to-sell-internationally)) and payment acceptance. It’s on you to shape your go-to-market strategy and partner with payment providers who stay on top of regulations globally.

**Key Takeaway: You need a partner who will stay on top of global regulations** Payment regulations (like sales tax regulations) can dramatically impact your revenue performance in regions across the world.

## Your software business depends on payment acceptance

We’ve outlined the underlying mechanics behind how payments fail, and the infrastructure needed to improve performance and capture revenue from what you’ve already sold:

  * Validation
  * Volume
  * Routing
  * Retries
  * Local acquirers
  * Currencies
  * Regulations


Unlike other global online sellers (like e-Commerce and marketplaces), most software companies don’t invest in optimizing this workflow like they do into other core revenue-generating workflows (like their signup flow, subscription billing, or lead scoring).

To optimize this needs a dedicated engineering and finance team. You can either build this all out yourself (with all the tooling and headcount that will take) or [partner with a provider that can optimize your payment acceptance ](https://www.paddle.com/features/payment-acceptance).

At Paddle, we’ve had an entire engineering team working on improving payment acceptance through all the strategies we’ve talked about today. If you’re exploring options to how you can improve payment acceptance in your software business, [talk to one of our payment acceptance experts today](https://www.paddle.com/demo).

## What’s the value to my business of improving payment acceptance? 🤷

Small improvements in monthly performance compound over time.

  * **1% improvement** in monthly subscription renewals drives over **10% more revenue** in 12 months
  * **2% improvement** in monthly subscription renewals drives over **21% more revenue** in 12 months
  * **3% improvement** in monthly subscription renewals drives over **30% more revenue** in 12 months


And that’s just payment acceptance. There are at least eight strategies we’ve seen to drive up [net dollar retention](https://www.paddle.com/blog/net-dollar-retention) for SaaS businesses and make more money from what you’ve already sold.

Curious to see how much revenue upside you could see?

👉 **[Try the dollar retention calculator.](https://paddlecom.typeform.com/to/NDPYQ3)**

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)