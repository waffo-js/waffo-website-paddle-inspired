---
title: "PSD2: What SaaS Companies Need to Know to Get Compliant"
description: "The second Payment Services Directive in the EU will be coming into force this September (PSD2). Its arrival will make increased security around payments made online - known as Strong Customer Authentication (SCA) - mandatory for many online payments. You’ve still got time to make sure you’re on top of this new legislation, so let’s take a look at what this means for SaaS companies to help you understand the steps you need to take to ensure your business is compliant."
source: "blog/psd2-get-compliant.html"
---

# PSD2: What SaaS Companies Need to Know to Get Compliant

![](https://images.prismic.io/paddle/683935ba-533a-4682-906c-88bb428eaf12_mike-wakeling.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Mike Wakeling](/resources/author/mike-wakeling)

Share

[](https://x.com/intent/tweet?text=PSD2%3A%20What%20SaaS%20companies%20need%20to%20know%20to%20get%20compliant%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpsd2-get-compliant%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpsd2-get-compliant)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpsd2-get-compliant&title=PSD2%3A%20What%20SaaS%20companies%20need%20to%20know%20to%20get%20compliant&source=)

The second Payment Services Directive ([PSD2](https://ec.europa.eu/info/law/payment-services-psd-2-directive-eu-2015-2366_en)) takes effect on September 14, 2019. From this date, banks will be able to decline any payment where Strong Customer Authentication (SCA) is not gathered when they request it.

SCA can be obtained when taking a payment by authenticating two of the following with the customer:

  * Something they are - like a fingerprint or other biometric info
  * Something they own - like a specific mobile device
  * Something they know - like a password


![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

## Who does it impact?

PSD2 primarily comes into play when both the customer and the company from which they’re making a purchase are based in the EU. The customer will need to have their card issued from an EU account and the company must have a merchant account in the EU. However, it’s recommended that even companies outside of the EU are ready to collect SCA when requested, as banks can ask for it at any time.

## What does PSD2 mean for SaaS recurring billing?

There’s no denying that recurring payments are likely to bear the brunt of PSD2. Although the recurring payment exemption exists, there are often times when a subscription amount changes, or the bank may not honor this exemption at all. In this instance, a way of collecting authentication for the payment will be required.

Here’s a quick overview of the ways you can make your recurring payments PSD2 compliant whilst maintaining the best possible user experience:

### Recurring payment exemption

If a subscription is always for the same amount - a regular occurrence in SaaS -**it’s advised that you apply the recurring payment exemption when processing the payment.** With this exemption, it’s likely that the bank will not request SCA. Exemptions will not always be granted, though, so you’ll need to be ready if SCA is requested (see ‘Authentication dunning’ below). 

### Merchant Initiated Transactions

A Merchant Initiated Transaction (MIT) takes place when the customer is not present in a purchase flow. One of the most common instances of this will be [subscription renewals](https://www.paddle.com/resources/subscription-renewal).

MITs will not always be exempt. You’ll need to have collected SCA as part of the initial transaction, so **we recommend enabling 3DS for all subscription sign-ups** , even if you could get an exemption (such as the low amount exemption). This ensures you’ll always have SCA associated with the subscription, so you won’t need to authenticate with every renewal. 

Another potential complication is that SCA gathered with an initial payment is ignored if a payment has not been taken against the subscription for 1 year. This can complicate yearly subscriptions or instances where companies are vaulting a card for occasional later use. **For yearly subscriptions, the recommendation is to send a pre-billing email around a week before the renewal is due.** In this email, you can provide a link for the user to authenticate in advance of you taking the payment, ensuring it succeeds when you process the renewal a week later. When circumstances don’t allow this, you’ll need to have built a solution for gathering authentication when it is requested and the customer is not present. This brings us to…

### Existing subscriptions

Existing subscriptions made under previous regulations will not require SCA in order to be renewed after September 14, 2019.

There are still some unknowns here. It’s possible that the 1 year rule mentioned above still applies, so you may still get asked for SCA if payment has not been taken in the last year. Our advice? **Make sure you have a system in place to gather SCA if you’re asked for it!**

### Authentication dunning

If SCA is requested and you don’t have the customer in a checkout, you’ll need a way to get them to authenticate the payment. We’re calling this ‘authentication dunning’. When you process a recurring payment and SCA is requested, you’ll need a way to get them into 3DS to authenticate the payment. **We recommend sending them an email and/or an SMS message containing a link to authenticate.**

This is purely for the purpose of gaining SCA for their recurring payment, so be sure you make that clear in your wording - you don’t want them to think they’re being asked to sign up again.

## How 3DS can collect SCA for you

PSD2 only applies to card payments. There are payment methods that already collect SCA, such as Apple Pay, which requires the customer to have the device belonging to them and to complete a biometric scan.

For payment methods that don’t already collect SCA, however, it’s important to put measures in place. **You can integrate 3D-Secure (3DS) for this.** 3DS v.1 has been around for a while now, although it hasn’t been great when it comes to user experience, with users needing to remember passwords or use physical card devices to verify their identity. Thankfully the latest version of 3DS (V2) is now on the horizon. Although it’s been around for the last year, adoption has been slow. 3DS v.2 does offer a much better user experience, however, as it can be embedded in the payment flow and often authenticates with methods such as SMS codes or push notification, so customers don’t have to remember passwords.

## Scope and exemptions

### In/out of scope

A transaction is ‘in scope’ when the customer and company have accounts in the EU. However, it’s important to know that there are some circumstances where, even if this is true, the transaction can be ‘out of scope’. This is the case when:

  1. The company and/or customer has an account outside of the EU.
  2. When it’s a Merchant Initiated Transaction (MIT) - a transaction where the customer is not present, such as a subscription renewal.
  3. When it’s a Mail Order/Telephone Order (MOTO) Transaction - a transaction which happens over the phone or by post.


If a transaction is ‘out of scope’, you should not be asked for SCA by the issuing bank, although it is possible that they will still ask for SCA as it’s at their discretion to do so.

### Exemptions

Exemptions can be applied for when a transaction is ‘in scope’. There are four types of exemption:

  * Low amount exemption - when the payment amount is less than 30 euros.
  * Whitelisted merchant exemption - some issuing banks will support whitelisting, where customers can add trusted companies to a list, so their next transactions skip authentication.
  * Recurring payment exemption - when it’s for a recurring payment of exactly the same amount.
  * Low risk exemption - when the merchant’s acquirer has a low fraud rate, the bank will allow higher transaction values without requiring SCA


You can apply for these exemptions when you authenticate a payment. Not all issuing banks will treat exemptions the same way and, although you may qualify for one, the issuing bank will honor it at their discretion. Paying attention to how exemptions are applied per BIN (bank identification number: the first 4-6 digits of a card number) will be an area to analyse in the future. Because of this, **picking the right exemption to apply for will become a big lever for optimizing payment acceptance and conversion rates.**

## Readiness checklist

  * Make sure you have a system in place to gather SCA if you’re asked for it.  

  * Enable 3DS for all subscription sign-ups.  

  * If SCA is requested and you don’t have the customer in a checkout, send them an email and/or SMS message containing a link to authenticate.  

  * If a subscription is always for the same amount, apply the recurring payment exemption when processing the payment.  

  * For yearly subscriptions, send a pre-billing email around a week before the renewal is due with a link for the user to authenticate in advance of you taking the payment.


## The big take-away

If you take one thing from this post, it’s that readiness is key! It’s vital to **be ready to collect SCA whenever it’s asked for** , even for recurring payments. Don’t forget to always collect SCA if it’s a subscription or if you want to vault the card for later use. Oh, and make sure you allow for the fact September 14 is a Saturday!

Paddle is here to help you overcome every legal hurdle, from sales tax requirements to the forthcoming PSD2. To find out more about how Paddle can help you take the pain out of payments and billing, [book a demo today](https://www.paddle.com/demo).

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)