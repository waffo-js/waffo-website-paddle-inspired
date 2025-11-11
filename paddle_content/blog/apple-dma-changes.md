---
title: "Apple DMA Changes - what this means for in app purchases"
description: "At the end of January, Apple announced their plans to comply with the EU’s Digital Markets Act (DMA). The changes are currently in beta and will go live with the release of iOS 17.4 in March."
source: "blog/apple-dma-changes.html"
---

# Apple DMA Changes - what this means for in app purchases

![](https://images.prismic.io/paddle/683935ba-533a-4682-906c-88bb428eaf12_mike-wakeling.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Mike Wakeling](/resources/author/mike-wakeling)

Share

[](https://x.com/intent/tweet?text=Apple%20DMA%20Changes%20-%20What%20this%20means%20for%20in-app%20purchases%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-dma-changes%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-dma-changes)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-dma-changes&title=Apple%20DMA%20Changes%20-%20What%20this%20means%20for%20in-app%20purchases&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

[**This blog refers to changes made in 2024. For information on Apple's response to the DMA in it's 2025 guidelines, click here.**](https://www.paddle.com/blog/apple-revises-eu-app-store-rules-what-developers-need-to-know-2025)

At the end of January, Apple announced their plans to comply with the EU’s [Digital Markets Act](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en) (DMA). The changes are currently in beta and will go live with the release of iOS 17.4 in March.

Although on the face of it, these changes may seem positive and a move in the right direction, unfortunately many caveats, restrictions, and fee changes make it much less appealing, especially if you would like to use a Merchant of Record like Paddle. To use the new capabilities, you must opt-in to a new fee structure in the EU. This reduces Apple’s commission, but it also introduces new fees which have the potential to punish any successful apps.

## Paddle’s summary

At Paddle, although we are pleased to see some progress in this space we don’t believe these changes are in the spirit of the DMA and are unlikely to result in the fair playfield we were hoping for. Unfortunately, the fee structure and the added friction to the buyer purchasing experience (due in part to Apple’s “disclosure sheet”) will likely discourage many developers from moving away from Apple’s IAP solution.

Due to this, Paddle will not yet create an iOS SDK to power in-app payments within App Store distributed applications. We will be awaiting more flexibility and attractive pricing from Apple to provide a better opportunity and incentive for developers. Hopefully, this comes with other countries introducing similar regulations, like the UK and Japan.

We are disappointed that we can’t deliver a solution right now but we are still exploring the opportunities presented by the changes. If you want to chat with us about this, you can reach out at [iap@paddle.com](mailto:iap@paddle.com)

We understand these new rules are confusing and often misinterpreted - it took us a long time and many debates to understand them ourselves! You can see our overview and breakdown of the changes below.

## The Changes

Under the proposed changes, which still may be challenged as invalid under the DMA, developers can choose to either: 

1\. Operate under the same status quo current terms and fee structure, and the new fees introduced won't apply; or 

2\. Irrevocably opt-in to the new EU Addendum with the new restrictions and fees. This means if you opt into the new structure you will be unable to opt-out.

Here is a quick overview of what that would look like:

  1. Sideloading of apps will now be possible. This means you will be able to download apps outside of the Apple App Store (only approved Alternative App Marketplaces)
  2. Alternative App Marketplaces will now be allowed to sell and distribute apps to iOS users, similar to the “Amazon App Store” on Android devices.
  3. When installing an app from outside of the Apple App Store, a user will be shown an App Installation Sheet which will display details of the app they are installing. These details are taken from the notarization process.
  4. Alternative Payment Service Providers can now be used for in-app payments. These alternative PSPs must have a native in-app payment integration and cannot use a web view to show a payment form. But if you want to use this feature, Apple requires that a warning is displayed in the form of a “disclosure sheet” stating that Apple’s “secure payment system” is not supported.
  5. You can now link to your website from within your app and you are also allowed to advertise promotions exclusive to your website. However, there are a lot of restrictions around how this looks and what wording you can use, including a mandatory warning pop-up that states that Apple is not responsible for the privacy and security of your website. This is very similar to the changes Apple made in the US recently.
  6. You must report third-party transactions (from alternative PSPs in-app, and those made on your website after a user has clicked the link in your app) back to Apple, so they can charge their fee. Apple has broad audit rights to check.


## New Fee Structure

These new fees replace the existing 30% Apple fee in the EU (or 15% for smaller developers and subscription renewals in their second or subsequent years). You can choose to move to these new fees, or remain on the existing ones. If you want to use _any_ of the new capabilities in the EU, you _must_ opt-in to the new fees.

The new fee structure splits the single fee into three separate fees:

  * Apple commission fee
  * Optional payment processing fee 
  * New Core Technology fee for app installs


Find a full breakdown of these fees below.

### Apple commission fee _(10-17% for all transactions)_

iOS apps on the EU App Store will pay a reduced commission of either:

  * 10% (for those on the current 15% fee for smaller companies, and for subscription renewals after their first year)
  * or 17% for developers with high revenue (instead of the 30% they currently pay)


This is charged for all purchases as a result of the customer being acquired via the Apple App Store, including:

  * In-app purchases
  * Purchases a user makes on your website within 7 days of clicking an in-app link
  * Future renewals of any subscriptions started this way


**The payment system you use has no impact on this fee.** Apple will force you to report the result of every in-app purchase click, and any click to your website.

### Payment processing fee _(3% if using Apple’s IAP)_

iOS apps on the App Store can use the App Store’s in-app purchase payment processing for an **additional 3% fee**. To avoid this fee from Apple, developers can process payments with an Alternative Payment Service Provider within their app, or link to their web store. They would still need to pay the alternative PSP’s fee, which might be higher than Apple’s 3%.

It’s important to remember this 3% is in addition to the 10-17% Apple is already receiving for each payment taken on an app. But if another provider wants to compete, it’s the 3% they will be compared to. Financially, it’s not possible to offer a viable merchant of record service at this rate.

### Core Technology Fee _(€0.50 for every install after 1,000,000 installs)_

For _very_ high-volume iOS apps distributed from the App Store and/or via an alternative app marketplace, developers will pay €0.50 for each first annual install per year _after_ the first million installs. 

**The first annual install** refers to the first time an app is installed by an account in the EU within a 12-month period. After each first annual install, the app may be installed any number of times by the same account for the next 12 months with no additional charge.

The Core Technology Fee was put in place to ensure they can still generate revenue for successful apps selling through alternative app marketplaces. They will also charge this fee even if the app is free. 

### Calculating fees

Apple has a [fee calculator](https://developer.apple.com/support/fee-calculator-for-apps-in-the-eu) to help developers figure out whether they should switch to the new fee structure in the EU.

## Alternative App Marketplaces

Alternative App Marketplaces is a new concept introduced to allow users to install and support software on iOS devices, access data across a catalog of apps, manage users’ purchases and subscriptions, and so on. App Marketplaces are given scope to behave like an App Store in a way that is compatible with Apple’s infrastructure, without having to charge the same fees.

To create an Alternative App Marketplace, you must apply for the entitlement from Apple, meeting their requirements detailed [here](https://developer.apple.com/support/alternative-app-marketplace-in-the-eu/). The requirements are pretty onerous and will be a significant barrier to many indie developers wanting to create a new App Store.

Alternative App Marketplaces _cannot_ be listed on the Apple App Store, and can _only_ be downloaded from the Marketplace developer’s website. 

When downloaded, the screen displayed will look like this:

![](https://images.prismic.io/paddle/65d4e4323a605798c18bf7cf_Untitled.png?auto=format%2Ccompress%3Fauto%3Dcompress%2Cformat&rect=0%2C0%2C573%2C1174&w=1200&fit=max)

When purchasing within an Alternative App Marketplace, paying for it (if applicable), and installing the app, Apple will show an App Installation Sheet. 

Here is the example they give on their website. The details displayed will be taken from the new Notarization process.

![](https://images.prismic.io/paddle/7a754010-34a1-4348-8b76-8d88e1540d3d_Untitled+%281%29.png?auto=format%2Ccompress&fit=max&w=3840)

## Alternate payment processing

In-app payments from other Payment Service Providers are now permitted within iOS apps distributed by the App Store for EU buyers. When paying with one of these instead of using the App Store’s IAP functionality, the 3% Apple processing fee will not be included (as we've explained above).

Integrations with Alternative PSPs for in-app payments come with some restrictions:

  1. You cannot have both Alternate PSPs and Apple IAP in the same storefront, you have to pick which one to display to EU customers (configurable by country). You cannot allow customers to choose.
  2. The in-app payment flow must be native (i.e. fields within the app) and cannot use a web view to facilitate the collection of payment details (so you can’t load your web store in your app, for example).
  3. When the user clicks to purchase, Apple will display a “disclosure sheet” when a payment is initiated from an alternative PSP (shown below). You can only show payment fields to the user if they click “Continue”. The idea is to warn your customers that they are purchasing outside of the Apple ecosystem, but in many cases, this will also hurt conversion rates.

![](https://images.prismic.io/paddle/ZfB4XkmNsf2sHhst_AlternatePSP-AppleDMA.png?auto=format%2Ccompress&fit=max&w=1920)

## Linking to your website

As we saw with the recent changes in the US in response to Apple’s litigation with Epic Games, you can now link to your website from within your application in the EU. There are a set of requirements this link has to follow. It must:

  * Go directly to your webpage without any redirects, intermediate links, or landing page
  * Open a new window in the default browser on the device, and may not open a web view
  * Be a static link (always the same) and not pass additional parameters in the URL
  * Be submitted with your app to the App Store (and resubmitted if the URL changes)
  * Follow the language and design requirements provided by Apple materials


The language and design requirements are as follows:

  * The copy must follow one of the templates defined by Apple [here](https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/)
  * The button must follow the “plain button” style and cannot be contained in a shape (i.e. it must look like a link, not a button)


Here are some examples from Apple:

![](https://images.prismic.io/paddle/0846a350-508c-4a4e-8976-7eb35434d527_Untitled+%283%29.png?auto=format%2Ccompress&fit=max&w=3840)

When the link is clicked, Apple will show a “disclosure sheet”. If the user clicks “Continue”, the website will be opened in a new Safari window.

As per the US rules, all purchases on the website made by the customer within 7 days of clicking the in-app link are charged the Apple Commission fee. This fee is also charged for all future renewals for subscriptions started within these 7 days.

![Apple disclosure sheet - Apple DMA](https://images.prismic.io/paddle/ZfBtD0mNsf2sHhmk_Appledisclosuresheetv2.png?auto=compress%2Cformat&fit=max&w=1920)

## Reporting transactions to Apple

It is a requirement that all transactions that don’t use Apple’s IAP must be reported back to Apple. This includes any transactions via alternative PSPs, as well as transactions occurring after a user clicks an in-app link to your website. It also includes all subscription renewals for subscriptions started from either of those sources.

This is to be done through a new [External Purchase Server API](https://developer.apple.com/documentation/externalpurchaseserverapi) Apple has created. You use the API to let Apple know the result of the transaction, providing details of the transaction, including a unique token that Apple provides every time you show an alternate PSP form, or click a link to your website. 

**Apple expects you to return this transaction data for each token issued, regardless of whether a transaction has been completed**. It has exceptionally broad audit rights to review the practices of the company to ensure it has complied with this requirement.