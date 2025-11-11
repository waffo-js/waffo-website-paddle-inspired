---
title: "Why your SaaS payments are failing and what you can do about it"
description: "The first step to stopping payment failure is to understand why it’s happening in the first place. Here are 6 reasons payments fail and what you can do about it."
source: "blog/6-reasons-for-low-payment-acceptance-in-saas.html"
---

# Why your SaaS payments are failing and what you can do about it

![](https://images.prismic.io/paddle/683935ba-533a-4682-906c-88bb428eaf12_mike-wakeling.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Mike Wakeling](/resources/author/mike-wakeling)

Share

[](https://x.com/intent/tweet?text=6%20reasons%20your%20SaaS%20payments%20are%20failing%20and%20what%20you%20can%20do%20about%20it%20%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2F6-reasons-for-low-payment-acceptance-in-saas%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2F6-reasons-for-low-payment-acceptance-in-saas)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2F6-reasons-for-low-payment-acceptance-in-saas&title=6%20reasons%20your%20SaaS%20payments%20are%20failing%20and%20what%20you%20can%20do%20about%20it%20&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

Understanding why payments fail is the first step to improving your [payment acceptance rate](https://www.paddle.com/blog/payment-acceptance), fixing your processes, and capturing more revenue. 💸

We looked at our data from over 5,000 software businesses to uncover 6 reasons SaaS payments fail and what you can do about it.

## 1\. Card-not-present transactions

Online card payments or “card-not-present” (CNP) transactions are far more likely to fail than those made in person. 

This is because, without the physical card (and often the added complication of thousands of miles between the buyer and the business), it’s easier for fraudulent transactions to take place. To combat this, banks tend to take an “if in doubt, decline” approach which causes genuine transactions to fail, bringing overall payment acceptance down. To put this in perspective, for every $1 in actual fraudulent online payments, $25 of genuine online payments are falsely declined. 

For SaaS businesses at the mercy of online payments, this can be a big problem, especially at the point of renewal when neither the card nor the customer is present. At this point, the customer can’t quickly react to the payment decline and try the payment again, [causing them to churn](/resources/churn-causes). 

### What can you do about it? 

To prevent CNP transactions from lowering your subscription payment acceptance rate, you need to have retry logic built into your payments and billing system. This way, you’re not reliant on the customer seeing a decline notification and taking action.

Alternatively, you can use a service that offers payment routing. This involves using multiple acquirers so that you can send the transaction through the ‘route’ (or the acquirer) that’s most likely to be successful. 

The other side of this is taking steps to make sure payments aren’t flagged as fraudulent in the first place. For this, you need: 

  * Low fraud and [chargeback rates](/resources/chargebacks)
  * A high volume of transactions to show you’re a trusted seller 


To achieve this you can: 

  * Hold out and build up your payment volumes as you grow – improving your payment acceptance over time 
  * Seek out fraud protection tools and proactively look at optimizing for reduced chargebacks
  * Sell through a reseller, and utilize their large payment volumes and built-in fraud and chargeback prevention


## 2\. Lack of funds 

Perhaps unsurprisingly, a lack of funds is one of the most common causes of payment failure. (Paddle data shows it accounts for around 26% of all failed card payments.) 

It’s particularly common for payments made by credit card (for example prepaid cards or those with a spending limit in place). 

For subscriptions, when payments fail for this reason it not only means losing immediate revenue but it can also cause customers to churn completely, without intending to – this is known as [involuntary churn](/resources/reduce-voluntary-and-involuntary-churn).

### What can you do about it? 

Retry subscription payments, either with your own built-in logic or through that of your payment or subscription billing provider. Most subscription billing platforms offer time-based follow up but some offer smart retries – using logic to learn behavior patterns and retry payments at the most optimal time for success. 

You should also consider allowing your customers to pay via payment methods where a lack of funds is less likely to be an issue. For example:

  * PayPal, can draw from multiple sources of funds (like credit cards and bank accounts). 
  * ACH debit in the US (or direct debit in other markets) takes funds directly from your customers’ bank account – which helps avoid credit limits being an issue.


## 3\. Incorrect or missing payment information

If the payment request has incorrect or missing information, the payment will fail. 

This can be a particular problem for recurring card payments, as cards can be lost or stolen and they expire (on average) every 36 months, all of which cause a change in card details. 

### What can you do about it?

At the checkout, you can take steps to prevent incorrect or incomplete information from being entered in the first place: 

  * Use card validation to set the parameters for the data you require for different payment methods (for example, card number or security number length). By building this logic into your checkout flow, you can determine whether or not the customer has entered the correct information and notify them if anything is missing  _before a_ payment attempt is processed.


For subscription payments:

  * Notify the buyer that the renewal date is approaching and remind them to check that their payment details are up to date. Make sure that in this communication you highlight the value of your product or service to avoid customers reconsidering their purchase decision. 
  * Ask your payment provider about ‘account updaters’. These sync updates to card credentials on file so that recurring payments can still be charged. Note: Whilst most providers do offer this as a service, they may pass on (or even markup) the associated costs. 
  * Ask your payment provider about network tokens. This is an alternative option to “account updaters”, in which you convert card data into a secure network token. Optimized by the card networks, network tokens don’t expire so you don’t have to worry about incorrect details, and your customers don’t need to worry about updating their information.


## 4\. Payment request formats

Successful payments are reliant on the relationships between banks – but unfortunately, there isn’t yet a standard approach for sharing information. This issue is compounded when you are processing cross border payments because they create longer payment chains, increasing the chance of error due to different messaging standards. 

This issue is recognised by the financial sector and common standards for financial transactions are being introduced under [ISO20022 ](https://www.iso20022.org).

Although ISO20022 will bring standardisation for 10,000 banks around the world, that still leaves around 300,000 others to contend with. 

### What can you do about it?

Managing this problem effectively is all about your [payments infrastructure](https://www.paddle.com/blog/revenue-delivery-infrastructure). You need the systems and processes in place that allow you to retry and resend payments through different routes. 

For cross border payments, the best results come when you bank locally. If acquiring banks (the bank that requests funds) and issuing banks (your customers’ bank connected to the card scheme) are in the same country, they are far more likely to have relationships with each other – and therefore payments are more likely to be successful.

Paddle data shows that with local acquiring there’s an increase of up to 20% in checkout payment completions and a 3% increase in subscription payment completions. 

Unfortunately, banking locally isn’t a quick fix if you do it yourself. Setting up local entities in multiple markets can take months. Then, for payment acceptance to improve, you need to build up your payment volume in each market so the banks see you as a ‘trusted seller’. 

Luckily, there are other options. Like selling through a payments platform that has these systems in place for you to utilize immediately.

## 5\. Currency conversion

If you only accept payments in one currency everywhere you operate, your payment acceptance rate could be taking a hit without you realizing. 

Currency conversion in the payment process makes for even longer payment chains and more potential fraud triggers.

### What can you do about it?

The solution here is a simple one: sell to customers in their local currency. Paddle data shows that the increase in payment acceptance for local currencies is anywhere from 1% to 11%, depending on the market. 

While the solution is simple, the execution can be difficult. Again, you’ll need to look at your payments infrastructure and the work involved in “switching on” a local currency – as well as evaluate the foreign exchange fees involved and any tax implications. 

## 6\. Financial compliance

Online payments are becoming increasingly regulated, meaning SaaS businesses have to manage more regulations globally and implement any requirements into their payment flow.

Strong Customer Authentication (SCA), for example, is a set of requirements under the [EU directive, PSD2 ](https://www.paddle.com/blog/psd2-comes-into-full-force)that requires multi-factor authentication for online payments. Unless the authentication (for example, a password, PIN, or fingerprint) is approved, the payment will fail. 

This is just one example, there are several others around the world. Brazil has restrictions regarding the use of local cards for international payments, and other countries, like Iran, have [sanctions ](https://www.paddle.com/support/countries-supported)that essentially cut them off from any wider payment network.

### What can you do about it?

Sadly, there isn’t a simple way to tackle this. The answer is to shape your payments infrastructure in a way that helps you stay compliant with regulations globally. 

Look at your current setup and ask yourself:

  * Do your current payment, subscription and other software partners help you manage compliance globally? 
  * Do they have processes in place to scan the horizon for upcoming regulations to make sure you don’t get caught out? 
  * Do they continuously optimize their processes to make sure payment acceptance isn’t impacted by any changes that come into effect?


![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)