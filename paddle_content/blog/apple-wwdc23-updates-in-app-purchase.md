---
title: "5 big updates to In-App Purchase from WWDC23"
description: "WWDC23 came with lots of announcements impacting the App Store, In-App Purchases, and subscriptions on iOS. Here’s what Apple showed beyond the flashy hardware."
source: "blog/apple-wwdc23-updates-in-app-purchase.html"
---

# 5 big updates to In-App Purchase from WWDC23

This year's Worldwide Developer Conference (WWDC) grabbed headlines mainly for its hardware reveals: new MacBooks, chips, and the hyped Vision Pro headset. But beneath all that excitement, there were several noteworthy announcements that directly impact the App Store and the App Purchase ecosystem.

![](https://images.prismic.io/paddle/25593093-6a95-4132-ab1d-61c5946f4277_stephen-ngo-headshot.png?auto=compress%2Cformat&fit=max&w=640)

Author

[Stephen Ngo](/resources/author/stephen-ngo)

Lead Strategy Manager

Share

[](https://x.com/intent/tweet?text=5%20big%20updates%20to%20In-App%20Purchase%20from%20WWDC23%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-wwdc23-updates-in-app-purchase%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-wwdc23-updates-in-app-purchase)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fapple-wwdc23-updates-in-app-purchase&title=5%20big%20updates%20to%20In-App%20Purchase%20from%20WWDC23&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

This event is primarily dedicated to app developers, who’ve built businesses through in-app purchases and subscriptions on iOS. So we’ve highlighted some of the most important updates you might have missed at [WWDC23](https://developer.apple.com/wwdc23).

## #1: More ways to generate demand and engagement through the App Store

The App Store is getting more functionality to help promote your app and in-app-purchases. The focus is no longer just on driving app downloads, but on re-engaging users and getting them to make repeated purchases and conversions.

Apple is increasingly relying on App Store advertising as a key lever for doing so, and so [attribution reporting is getting better](https://developer.apple.com/videos/play/wwdc2023/102/?time=3087), especially for post-click conversions — though still not as deep as what you’d get from vendors like Meta.

[App Store pre-orders](https://developer.apple.com/videos/play/wwdc2023/10015) are also receiving enhancements in App Store Connect, especially when it comes to region-specific publishing. You’ll now be able to soft launch your app in certain regions, even as they’re already on sale in other parts of the world.

###### Key announcements:

  * SKAdNetwork improvements to measure App Store’s impact on downloads, re-engagement and conversions after tapping on an ad
  * Enhancements to App Store pre-orders, especially for regional publishing. Allows you to simultaneously soft launch your app in some regions, while offering it in others
  * Redesigned “Availability” page in App Store Connect to help manage pre-orders and soft launches by region
  * Ability to [generate marketing and customer service API keys](https://developer.apple.com/videos/play/wwdc2023/10117/?time=703) to manage marketing metadata or respond to App Store reviews


## #2: Features to tailor product offers to each user, whether on the App Store or in-app

Apple’s In-App Purchase system is improving how it shows off your paid product offerings, with the intent of improving checkout conversion rates and monetization. These improvements are also being extended to your App Store product page.

The [first set of changes](https://developer.apple.com/videos/play/wwdc2023/10140/?time=483) revolve around in-app pricing pages: both the Product View and Subscription Store View. Through the StoreKit framework, developers can customize the list of paid products, and whether each product is shown or hidden. All of this can be personalized to each individual user’s purchase history or subscription status.

This Checkout customization functionality is being extended to your App Store product page through [promoted in-app purchases](https://developer.apple.com/videos/play/wwdc2023/10140/?time=58). When you show a list of your in-app purchases on your App Store page, you can tailor this based on similar logic to your Product View and Subscription Store View.

The Subscription Store View also comes with a [main CTA button](https://developer.apple.com/videos/play/wwdc2023/102/?time=3068) which highlights the primary offer you want to promote to the user. Developers can also personalize this for each individual user, based on purchase history or subscription status.

###### Key announcements:

  * The Product View and Subscription Store View (Apple’s terms for in-app pricing page) is administered through Apple’s StoreKit framework, allowing you to deploy these with one line of code
  * Can select and customize an offer for the main CTA on the product view — ensuring you display the right offer to the right user, based on purchase history or subscription status
  * New StoreKit 2 APIs for promoting a list of in-app purchases on your App Store product page. You can customize the list of which products are shown or hidden, and how they’re ranked based on an individual user’s purchase history or subscription status
  * StoreKit 2 updates the data model, so you can see which “Storefront” the user saw when they purchased or subscribed


## #3: Big updates to global pricing functionality

App Store Connect is giving you more flexibility to how you set prices globally. Developers have options to automatically adjust prices, whether they want to “set it and forget it” or “get into the weeds”.

The easy route is to [set global prices](https://developer.apple.com/videos/play/wwdc2023/10014/?time=57). First, you select and set prices for a base region — this price is the benchmark by which all other regional prices are set. App Store Connect will then auto-adjust your prices in every other region based on foreign exchange and tax rates.

This does not [localize based on regional users’ willingness-to-pay](https://www.profitwell.com/benchmarks-for-localized-pricing), as we’d recommend; but it does ensure that you price for a certain Average Revenue per User, if that’s a target you’re aiming for. If you haven’t selected a base country or region, Apple will use your current price in the United States as its baseline until you specify otherwise.

A more advanced option is [custom prices](https://developer.apple.com/videos/play/wwdc2023/10014/?time=1226), which let you select a specific price point for every region in which you sell. This allows you to optimize each region’s pricing based on willingness-to-pay, foreign exchange rates, and taxes. But this means that Apple puts the responsibility on app marketers and developers to make adjustments in every region, which can be a big task.

Finally, App Store Connect allows you to set [temporary prices](https://developer.apple.com/videos/play/wwdc2023/10014/?time=966), in a given region, for a finite period of time. This can be useful for running promotions or conducting price elasticity tests.

Now, you can’t set any price point you want per se; Apple has a list of supported pricing conventions for any supported currency that you must select from. But it’s [increasing the number of supported price points](https://www.apple.com/newsroom/2022/12/apple-announces-biggest-upgrade-to-app-store-pricing-adding-700-new-price-points) from 200 to 900, granting much more price flexibility.

In order to provide all this flexibility in [App Store Connect API 2.3](https://developer.apple.com/documentation/appstoreconnectapi/app_store_connect_api_release_notes/app_store_connect_api_2_3_release_notes), Apple will be deprecating older versions of the App Store Connect APIs later in 2023.

###### Key announcements:

  * Set global, custom, or temporary prices — all from App Store Connect. You can also fetch and update this data using appPricePoints in the App Store Connect APIs.
  * Global: Set a “base region” with a base price, and then Apple will auto-adjust in all other regions where you sell based on foreign exchange and tax rates. This does NOT localize based on regional users’ willingness-to-pay, but this works fine if you’re targeting a certain Average Revenue per User for your app.
  * Custom: Choose a custom price point for each region.
  * Temporary: Can set a temporary price point in a given region for a finite period of time, helpful for running promos or pricing tests.
  * Expanded list of 900 price points for app purchases or subscriptions, available across 44 categories.
  * [Deprecating some older App Store Connect pricing APIs](https://developer.apple.com/videos/play/wwdc2023/10014/?time=1549) later this year.


## #4: Improvements to subscription management and retention flows

While Apple’s In-App Purchase system has historically optimized for the use cases of non-recurring B2C apps and products, its subscription functionality has been lackluster. But some sorely-needed features are finally getting introduced for recurring revenue billing models.

Apple is launching two incremental improvements for customers to manage their existing subscriptions, and for app developers to retain their subscribed customers through failed payment recovery.

First, StoreKit is adding a [“Manage Subscription” sheet](https://developer.apple.com/videos/play/wwdc2023/10140/?time=593) that shows a customer their currently active subscriptions for an app, without leaving the app. From this view, customers can also upgrade, downgrade, or cancel their subscriptions. Developers are encouraged to use this by adding a “Manage Subscriptions” option within their app that calls the appropriate [StoreKit method](https://developer.apple.com/documentation/storekit/appstore/3803198-showmanagesubscriptions).

The [Message API](https://developer.apple.com/documentation/storekit/message) in StoreKit 2 is also adding support for a [“Billing Issue” message sheet](https://developer.apple.com/videos/play/wwdc2023/10140/?time=339). This can be displayed when a user’s subscription fails to renew as a result of a failed payment, and prompts users to update their payment method without leaving the app. This is a big step for subscription-based apps whose UX is contained mostly within the app, but it still leaves big gaps for brands whose footprint extends to the web, email, SMS, and other channels. Fortunately, [solutions for reducing delinquent churn](https://www.paddle.com/retain) on these channels already exist.

###### Key announcements:

  * Adding a new in-app “manage subscription” sheet to help users view and modify their existing subscriptions and subscription groups within the app UX. You can pick the relevant subscription group in your app’s context, and show which other plan tiers that users can upgrade or downgrade to.
  * Message API in StoreKit 2 now allows you to display a “Billing Issue” message sheet when a user’s subscription fails to renew, allowing users to update their payment method without leaving your app.


## #5: API updates to make building and testing in-app purchases easier

Lastly, Apple is adding a multitude of API and testing improvements to improve quality of life for app developers. See below for a non-exhaustive list.

###### Key announcements:

  * Introducing [Get Transaction Info endpoint](https://developer.apple.com/videos/play/wwdc2023/10141/?time=309), to get info for a single transactionId (instead of having to parse through all data from "Get Transaction History" API endpoint.
  * Can now call whole Transaction History, All Subscription Statuses, or All Refund History using [just TransactionID](https://developer.apple.com/videos/play/wwdc2023/10141/?time=392) (not only original TransactionIDs).
  * Subscription status notifications: [new Status field](https://developer.apple.com/videos/play/wwdc2023/10141/?time=622) to clearly indicate latest status of subscription (which you previously had to infer). Included in every notification for auto-renewing subs, so you don't have to keep calling Get All Subscription Statuses API endpoint.
  * Introducing [new “onlyFailures” optional request field](https://developer.apple.com/videos/play/wwdc2023/10141/?time=725) to "Get Notification History" endpoint, so you only have to parse through relevant transactions in case of a server failure.
  * [Deprecating APIs](https://developer.apple.com/videos/play/wwdc2023/10141/?time=1009): App Store Server Notifications V1, and verifyReceipt. Plan to migrate to App Store Server API, and App Store Server Notifications V2. APIs testable in sandbox, and now releasing App Store Server Library to test calling API endpoints and verifying data.
  * [TestFlight is adding functionality](https://developer.apple.com/videos/play/wwdc2023/10117/?time=239) to see the most recent device and OS on which a beta app was installed, to filter by tester data to manage segments of users, and to bulk add or remove testers.
  * App Store Connect is adding ability to [test Family Sharing](https://developer.apple.com/videos/play/wwdc2023/10117/?time=353) by combining up to 6 sandbox test accounts into a Family Group.


## What else would you like to know?

With dozens of [technical updates at WWDC23](https://developer.apple.com/wwdc23/sessions) and [regulators progressing](https://www.theverge.com/2023/7/4/23783790/eu-digital-markets-act-gatekeepers-apple-google-amazon-meta-tiktok) on enforcement of new rules, it can be time-consuming for busy app developers to know how market changes impact them. Building a great product and running a healthy business is already enough of a challenge.

What questions do you have on WWDC23, the upcoming Digital Markets Act, or wider trends in the App Purchase Ecosystem? Email us with your questions at [iap@paddle.com](mailto:iap@paddle.com).