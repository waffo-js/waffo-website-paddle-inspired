---
title: "Rolling Out GDPR"
description: "A major new regulation, the GDPR, is coming into effect by the end of May, affecting how we handle the personal data of software buyers. We have taken our usual approach to rolling it out: handle most of its complexity automatically and provide you with the simple tools you need to manage it on your end."
source: "blog/rolling-out-gdpr.html"
---

# Rolling Out GDPR

![](https://images.prismic.io/paddle/1c534aa9-e4e0-479b-861c-513c72b0183a_harrison-rose.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Harrison Rose](/resources/author/harrison-rose)

Share

[](https://x.com/intent/tweet?text=Rolling%20out%20GDPR%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Frolling-out-gdpr%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Frolling-out-gdpr)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Frolling-out-gdpr&title=Rolling%20out%20GDPR&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

A major new regulation, the GDPR, is coming into effect by the end of May, affecting how we handle the personal data of software buyers. We have taken our usual approach to rolling it out: handle most of its complexity automatically and provide you with the simple tools you need to manage it on your end.

We exist to help software companies run and grow their business. One of the main ways we do this is by making sure that everything you need to sell your products is either really simple to use, or handled by us on your behalf. This allows you to focus on what’s really important, building your own products.

This is especially important when it comes to compliance, a topic which is as important as it is complex. A major new regulation, the [GDPR](https://www.eugdpr.org/), is coming into effect by the end of May, affecting how we handle the personal data of software buyers.

We have taken our usual approach to rolling it out: handle most of its complexity automatically by providing you with the simple tools you need to manage it on your end.

![](https://images.prismic.io/paddle/9ec85d18-1a4e-4129-af4f-30544f5e940a_abstract-sand+timer+2.png?auto=compress%2Cformat&fit=max&w=3840)

## What is the GDPR and why does it concern you?

The European Union (EU) is introducing a landmark regulation called the General Data Protection Regulation (GDPR in short) on the 25th of May.

The goal of GDPR is to give EU residents drastic improvements to their privacy rights and control over their personal data, and to protect them from privacy breaches and leaks.

Every organization that handles, markets or tracks the personal data of EU residents is concerned, even if they are not based in Europe. In the case of software companies which typically sell their products globally, this means that this new regulation will apply to everyone, no matter where they are based.

There are strong penalties in place for non-compliance: up to €20m or 4% of global annual turnover, whichever is higher.

Making sure we were compliant, and in turn that the personal data of the customers buying your products was treated correctly, whilst continuing to provide a great customer experience has been an important focus for us over the past few months.

Here are the main concepts of the GDPR:

  * **Personal data requires lawful processing**. This means that you shouldn’t buy email lists where you don’t know how consent was acquired, and we can’t enable newsletters to customers if we don’t know whether they have consented to them.
  * **Customers should specify exactly what communications they want to receive from you**. This means that the language explaining how you will contact them needs to be very clear and respect certain rules - leading to fewer unsubscribes and spam reports.
  * **Customers will have a right to transparency around the collection and processing of their data**. This means that they will be able to ask us for the data we store on them, and receive it in a simple format.
  * **Customers can request the right to be forgotten**. This means that if they ask us, we will remove all their personal data - letting you focus on the best customers.


Implementing all of this could be complex (just ask our in-house GDPR experts who have been looking into its correct application!). We’re rolling out changes to ensure that it is simple and straightforward for you.

## What Parts of Our Platform Does That Impact?

For the most part, the changes we make as an organisation to ensure we are GDPR compliant don’t impact the way you can use our platform. If you use our Audience feature, certain things will change.

Audience allows you to collect the email address of customers and build a marketing list. 

We automatically populate your Audience dashboard with users who start your checkout. You can also enrich that list with a newsletter form, an exit pop-up when the user mouses out of the page, or by directly uploading members via our API, for example new signups or free trial users.

## How Are We Rolling Out the GDPR and How Does It Affect You?

We are making changes to the way we store the personal data of the people buying your products, the way we collect their consent to let you access and use that personal data and the dashboard interface and API calls we offer around this.

Because we believe that the changes that GDPR introduces will contribute to making customer data safer online, we will treat customer data from non-EU residents the same way we treat EU residents. This means that US residents for example will benefit from the same level of protection as EU residents, even though they are not covered by the GDPR. This approach will also minimize complexity for you and your implementation: for example you won’t need to handle the case of an existing customer moving to the EU or leaving it.

Personal data from customers is available in 2 main ways in our platform:

  * As part of the Transaction data, to help you fulfill and support purchases. Nothing will change here.
  * As part of our Audience section, to help you market to customers and let them know of any upcoming news or promotional offers. This is where we are making changes.


### Changes to the way we collect consent from customers

When it comes to the different ways that we populate your Audience, we will no longer consider that marketing consent is opt-in by default. Customers will need to proactively decide to give consent.

In practice this means that each time personal data is collected - for example during the checkout flow or in-app via our SDK - we will ask for consent, which cannot be pre-ticked by default.

We are also removing the “Automatic” setting to the collection of marketing consent in our dashboard. If you used that setting, you will now be on the “Optional” setting which requests consent from the customer. The “Disabled” option, where you don’t want to collect consent in the first place, still exists.

Consent can now be collected in 2 ways:

  * Either you let us handle it, in which case we will display a GDPR-compliant checkbox on the checkout, localized in the language of the customer. To guarantee compliance this sentence cannot be customized.
  * Or if you are already collecting the email address yourself (to use with our Audience API, or to skip the first step of the checkout), you can pass the consent to us using marketing_consent: true in your implementation. We will work with you to make sure that your message and implementation are compliant, and monitor compliance as part of our usual quarterly reviews, as part of our regulatory requirements.


This approach ensures that the personal data you collect is stored in a compliant manner, protecting customers from bad data practices and yourself from the expensive fines.

If you’re using our Audience Add API you’ll need to modify your request to include extra parameters to indicate that you have collected consent in a GDPR compliant way.

### Changes to the personal data we collect

We will no longer expose the MAC and IP addresses of customers, and will remove these data points from all existing sellers. These are protected under the GDPR and do not present a sufficient business need to justify exposing them, which is why we are making this change.

### Changes to the macOS SDK

You will need to update to a new version of the SDK which will be released next week. This will make sure consent is collected correctly. From now on email addresses used for activations will not be added to Audience. Going forward we may look to add an opt-in for activation to collect marketing consent and addition to Audience.

### Changes to the audience section

The Audience section will now only show the people you can market to; those that have provided consent in a compliant way. However, your full list of customers (including those that _do not_ provide consent) can still be accessed from the full Audience report, Audience export, and the Transactions section. These reports clearly state who has opted in and who hasn't, to make it easy to select recipients for your marketing communications. 

Because past opt-ins are no longer compliant, we will be setting the consent status of EU customers to opted-out. This means those customers will no longer be shown in Audience, but will still be in the reports, as mentioned. You won’t lose any data but will be compliant with GDPR.

Going forward, if one of your customers has consented to receiving marketing communication, we will show them in Audience. When importing Audience members manually you must have consent to market to them, otherwise you will not comply with GDPR. This section will therefore clearly show who can be contacted.

Alongside the Audience changes we’re making it is much easier to see whether consent has been collected for a particular customer:

  * Notifications and fulfilment webhooks will include whether marketing consent has been collected when they return the customer’s email
  * Any API that returns a customer email will also include whether marketing consent has been collected. The following endpoints will be changed:  
undefinedundefinedundefined


This approach is fundamental to the GDPR: clear and compliant consent will be collected and stored, without any fears around data where this consent cannot be produced.

## When is this happening?

There are 4 main dates you should be aware of.

### 1\. We’ll be releasing a new version of the macOS SDK **next week**

This will ensure that customer marketing consent is collected in a GDPR compliant manner. 

### 2\. We are releasing most of these changes in our platform on the **18th of April**

This will mark the start of the transition period for you, during which you will be able to implement changes especially around collecting and passing consent, without any breaking changes.

### 3\. GDPR changes will be enforced on the **9th of May**

All non-GDPR compliant data, as explained above, will be removed. Going forward if consent is not passed to us we will assume that it wasn’t provided, thus the customer will not appear in Audience. Anything collected after the 18th April that is compliant will not be removed.

### 4\. The GDPR regulation comes into force on the **25th of May**

You will already be compliant thanks to the changes we’ve outlined. If you haven’t made any change to your integration, we will simply consider that customers did not pass consent, they will not appear in Audience, and there won’t be any breaking changes. We will be reaching out to any seller who still sends us personal data without explicit consent to ensure a they’re collecting consent in a compliant way.

## What’s next?

If you are interested in the way our platform complies with the GDPR, please take a look at our [GDPR readiness page](https://www.paddle.com/legal/gdpr).

If you have any questions regarding these changes or would like our help implementing them, just reach out to our [Customer Success team](mailto:vendors@paddle.com), we’ll be happy to help!

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)