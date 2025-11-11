---
title: "Payment Routing Part 1: Unifying the payments lifecycle"
description: "In this two-part series, we dive into the concepts we developed at Paddle to allow our Sellers to take advantage of payment routing with just one integration."
source: "blog/payment-routing-part-1-unifying-the-payments-lifecycle.html"
---

# Payment Routing Part 1: Unifying the payments lifecycle

![](https://images.prismic.io/paddle/ZgP3BLLRO5ile63L_Georgewilson.jpeg?auto=format%2Ccompress&fit=max&w=1080)

Author

[George Wilson](/resources/author/george-wilson)

Engineering Manager at Paddle

Share

[](https://x.com/intent/tweet?text=Payment%20routing%20part%201%3A%20Unifying%20the%20payments%20lifecycle%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-1-unifying-the-payments-lifecycle%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-1-unifying-the-payments-lifecycle)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-1-unifying-the-payments-lifecycle&title=Payment%20routing%20part%201%3A%20Unifying%20the%20payments%20lifecycle&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

_This is part one of a two-part series, where we explore the concepts developed at Paddle so our Sellers (our customers) can take advantage of payment routing with just one integration._

Paddle's [global payments solution](https://www.paddle.com/billing/payments) leverages various payment providers to efficiently process payments across different regions, ultimately driving better results for our users. 

In this article, we’ll explore how Paddle achieves this and explain the complexities of integrating with multiple payment service providers, and outline how we developed a unified payment lifecycle for our customers.   


## Paddle's payment solution

Paddle provides several payment method choices to our customers, and we integrate with multiple independent payment service providers (PSPs) to achieve this. What you might not know is that Paddle also holds several _Merchant Accounts_ in different regions around the world where we can accept payments.

A Merchant Account is a single bank account in Paddle’s name that is attached to global payment networks with the help of a PSP. The concept of opening Merchant Accounts to accept payments nearer to the end customer is called _local acquiring_.

Local acquiring presents some big benefits to Sellers who process international transactions. It means that more payments will be considered _domestic_ because both the _acquiring bank_ and the _issuing bank_ are within the same country or regulatory region. 

For our customers, also known as Paddle Sellers, this results in better payment acceptance rates overall (because international transactions are more likely to be declined) and lower fees from the payment networks.

In some cases, Paddle has integrations with multiple PSPs in the same region. At first, this might seem redundant because we’re already achieving local acquiring with one PSP, but there are additional benefits:

  * **Different providers offer different payment methods.** This allows us to enable more alternative payment methods for our Sellers.
  * **We have found significant differences in acceptance rates between PSPs even in the same regions** , which is most likely a result of providers using different acquiring banks. Therefore, we might make payments with cards issued in certain countries to be processed by a specific provider to improve acceptance rates.
  * **Redundancy is key.** If a PSP has a reliability issue, an outage, a regulatory issue, or even goes bankrupt, we must have alternative providers to maintain consistent service to our Sellers.


To take advantage of such a setup, we needed to build a system that was capable of choosing which _destination_ (we’ll use this term to mean a Merchant Account in a specific region using a specific PSP) a payment should be processed on. We call this “routing”.

**Figure 1 - High-level payment routing flow**

![](https://images.prismic.io/paddle/ZgQCO7LRO5ile68K_PaymentsDiagrams-Highlevelpaymentroutingflow.png?auto=format%2Ccompress&fit=max&w=1920)

But being able to route a payment to its destination isn’t enough. We found that we also needed to:

  * Accurately measure performance for all payment methods across all PSPs in all regions to fully understand the impact of our payments strategy.
  * Quickly change our payments strategy over time to improve performance, without requiring engineering changes, and to run experiments to influence new strategies.
  * Add integrations to new destinations quickly, and immediately measure performance accurately to maximize benefits.   


To achieve all this, we needed to standardize all of our integrations with payment service providers into one unified lifecycle.

### **A quick case study**

When assessing Paddle, [Motion VFX](https://www.paddle.com/customers/how-motionvfx-optimized-payment-processes) (the leading creator of plugins for Final Cut Pro and DaVinci Resolve) ran an A/B test between Paddle and their previous payments solution. They measured the conversion rate at the end of the checkout process – after a customer pressed “pay now”. The result was a 12% increase in conversions with Paddle. We attributed this increase to a better checkout experience and an increase in payment acceptance rates, made possible by the investments we made to strengthen our payment solution. 

## Unifying the payment lifecycle

Paddle’s Checkout provides a choice of payment methods and each payment method might require different PSPs to support local acquiring.

This payment setup can get quite complicated on its own and becomes a huge challenge when developing a routing system on top of it all. What we need is a consistent data model and API contract for all of our payment methods and integrations.

**There are a few reasons this is crucial:**

  * We want to directly compare different payment integrations fairly against each other. There’s no use routing some payments to one destination over the other if we’re not confident that they perform better.
  * We want to be able to add new payment methods, PSPs, and regional Merchant Accounts over time, and they should be able to take advantage of the existing routing, analytics, and retry features.
  * We want to provide consistent and meaningful experiences to all Paddle users when they interact with payment data in the dashboard, APIs, and reports, and for example, to understand payment decline reasons.


_The diagram below shows a simple hypothetical payment lifecycle. Paddle’s is a bit more complicated than this, but follows the same principles._

**White** = processing steps  
**Red** = final states of unsuccessful payments  
**Green** = final state of a successful payment

**Figure 2 - High-level lifecycle of a payment**

![](https://images.prismic.io/paddle/ZgVSIMt2UUcvBP-w_Paymentlifecycle.png?auto=format%2Ccompress&fit=max&w=1920)

Developing this was an engineering challenge, but one that Paddle considered truly worthwhile to unlock the value of local acquiring. We’ve done this work so our Sellers don’t have to.

The first challenge to overcome is the technical complexity involved in standardization because every PSP integration is different. It’s because not all payment service providers have SDKs, some use XML and others JSON. They can also have varying meanings attached to an HTTP status (or none at all!), and some necessitate a complex PCI-proxy setup to keep card data safe.

We found that the main ingredients required to unify these integrations are the following:

  * Firstly, we need a suitable data model to implement the “lifecycle” of a payment as a state machine. This is used for both the transactional processing of payments, and also as the basis of an analytics model which Paddle can use to compare the performance of all potential integrations.
  * Secondly, we need an API to move our payments through this lifecycle. It needs to be simple enough for other Paddle systems to interact with, but capable of accommodating specific features that might vary depending on payment method or the nature of the payment. For example, card payments require a unique approach to fraud detection, and also necessitate 3D-Secure. 
  * Finally, we need to make sure that each integration can describe the final outcome of a transaction in a shared language across all integrations. We call this “response mapping”. This lets us understand _why_ a transaction ended up with that particular outcome. A very common example of this is being able to identify an “insufficient funds” decline, or being able to differentiate between payment declines and system failures that can occur downstream.


With a unified payment lifecycle, we’re able to standardize payments from different PSPs, measure performance, and build a rules engine that determines how each payment gets routed. 

In the next blog post, we walk you through our rules engine, the two strategies we currently use, and outline some challenges and plans for payment routing at Paddle. 

[Read it here.](https://www.paddle.com/blog/payment-routing-part-2-developing-paddles-rules-engine)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)