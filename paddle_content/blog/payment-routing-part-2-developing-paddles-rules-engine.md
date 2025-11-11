---
title: "Payment routing part 2: Developing Paddle’s Rules Engine"
description: "In part 2 of this two-part series on payment routing, we explore the rules engine built to determine how payments are routed to their destinations, maximizing outcomes for our Sellers."
source: "blog/payment-routing-part-2-developing-paddles-rules-engine.html"
---

# Payment routing part 2: Developing Paddle’s Rules Engine

![](https://images.prismic.io/paddle/ZgP3BLLRO5ile63L_Georgewilson.jpeg?auto=format%2Ccompress&fit=max&w=1080)

Author

[George Wilson](/resources/author/george-wilson)

Engineering Manager at Paddle

Share

[](https://x.com/intent/tweet?text=Payment%20routing%20part%202%3A%20Developing%20Paddle%E2%80%99s%20rules%20engine%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-2-developing-paddles-rules-engine%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-2-developing-paddles-rules-engine)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fpayment-routing-part-2-developing-paddles-rules-engine&title=Payment%20routing%20part%202%3A%20Developing%20Paddle%E2%80%99s%20rules%20engine&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

_This is part two of a two-part series on payment routing, where we explore the concepts developed at Paddle so our Sellers can take advantage of payment routing with just one integration.[Read part one here.](https://www.paddle.com/blog/payment-routing-part-1-unifying-the-payments-lifecycle) _

Over the past year and a half, Paddle has added substantially more routing and retry logic to our [payments solution](https://www.paddle.com/billing/payments), added new payment methods, and opened several new Merchant Accounts to take advantage of local acquiring.  


To make this possible, we first needed to standardize payments from different payment service providers (PSPs), which we explored in the first blog post.   


Then we built out a rules engine to determine how payments are routed to their destinations, maximizing outcomes for our Sellers. In this blog, we’ll dive into how the rules engine works. 

  


## Rules engine for payment routing

Every time a new Paddle payment is attempted on our platform, information about the payment is sent to the rules engine which decides which Merchant Account and which PSP integration should handle the payment.

Paddle’s payments experts define and continually optimize active rules in the rules engine based on our data and analytics. They do this using our bespoke UI application that affords intuitive drag-and-drop controls to update the order in which rules should be evaluated.

It might be considered a luxury to have a UI to manage the rules, instead of treating them as business logic that is part of our payment solution. However, treating the rules as data rather than as code allows payment routing logic to be managed independently of Paddle’s engineering team.

**Figure 1 - High-level flow of payment routing and retries**

![](https://images.prismic.io/paddle/ZilTpPPdc1huKwbn_Paymentlifecycle.png?auto=format%2Ccompress&fit=max&w=1920)

To explain how the rules engine works, we will follow a hypothetical payment through the system step-by-step. The first step is to load the latest version of all our rules that were set using the UI.  


Each rule has a defined set of conditions which are basic logical statements that apply to a set of _dimensions_. Some examples of dimensions are payment method, payment amount, currency, card brand, card issuer, customer country, and payment type (this is how we differentiate between one-off payments and subscriptions). An example of a condition might be “Payment amount greater than 10”, and another might be “Card issuer equals NatWest UK”.  


If the transaction is a renewal payment for a subscription, we may also take into account which destination was used on previous attempts for the same specific payment method.  


The rules are _evaluated_ in sequence until a rule is found where all the conditions are met. We call this rule the _matched rule_. The matched rule provides the _destination_ which represents the PSP and Merchant Account.

The most basic rule might have a single destination, but rules can also have one of the following strategies that define __ multiple destinations, how those destinations will be attempted, and in what order.

### Fallback strategy

The fallback strategy of a rule allows us to set alternative destinations if the first destination could not accept the payment.  
In the “unified payment lifecycle” section in the [previous blog post](https://www.paddle.com/blog/payment-routing-part-1-unifying-the-payments-lifecycle), we talked about _response mapping_. One part of that process is deciding whether the failure reason is deemed suitable for retrying at a different destination. Some examples might be if there are system reliability issues or certain “soft declines” from the issuing bank.  
There is no limit to how many fallbacks can be defined in a rule’s strategy, but in practice we tend not to use more than two.

### 

### Weighted strategy

There are times when we might want to distribute payments matching the rule across multiple destinations. This is particularly useful if we are slowly rolling out a new merchant account. Still, the main benefit is being able to benchmark different destinations against each other to identify which destination drives better results under which conditions.   
For example, we might want to determine which PSP performs better for Norwegian credit cards purchasing subscriptions.

The next step for our hypothetical payment is to execute the strategy, choosing which destination we will use first.

In general, once we’ve contacted the PSP and mapped the response, if the payment does not succeed, we have the option of trying again. Depending on the specifics of the PSP, we may retry the payment at the same destination but with slightly different parameters. These tend to be small optimisations that Paddle has developed in partnership with our payment providers to help achieve better acceptance rates at the margin.

With the weighted strategy, the first step is to see which destination has been specified. Then, we attempt the payment against that selected merchant account. If that payment fails but it can be retried _and_ if the rule has a fallback strategy, then we will try again with the merchant account set in the fallback strategy. 

Once all the retries are exhausted, we have our final result of the transaction attempt. All outcomes of all attempts are saved for analysis which inform us of how we can improve our routing rules or retry behavior.

## Data-driven improvements to payment routing 

There’s not much use in developing a way to route payments if you don’t know what routing rules to deploy! 

As mentioned, we record the outcome of every payment in a unified manner for all payment methods and PSP integrations. This ensures we have a standardised understanding of what happened. We typically store the exact failure reasons and decline codes from the integration, and also our internal unified representation of the outcome.

Naturally, we will also store which payment method, PSP, merchant account, and Paddle legal entity was used. But just knowing this plus the outcome is not enough. We also store an identifier representing the matched rule. It’s also crucial to store a reference of the _version_ of the rule to make sure we can account for any changes made to the rule over time.

We store this data for every transaction, regardless of outcome. It is then replicated and made available in a data warehouse using a data pipeline developed by Paddle’s data engineering team.

Once prepared, Paddle’s product analysts use this information to conclude outcomes from split tests, produce new rules, and develop new hypotheses for testing.

Even if a conclusion on an A/B test is reached with a high degree of confidence, we must always maintain a small portion of payment attempts to the losing variant as a control group. This is because our payment partners actively develop their own integrations and risk rules over time. As we continually test, we are able to identify when we might want to reconsider our own rules.

## Challenges with multiple payment destinations 

It’s worth acknowledging some of the downsides of taking on the complexities of having multiple payment destinations.

Firstly, there are a lot of workflows to support, in addition to payments. Our integrations have to support fraud detection mechanisms, refund procedures, and different ways of managing disputes. Each integration, plus the complexity of the routing system itself, is a considerable engineering investment taken on by Paddle not just to set everything up, but also the ongoing cost to maintain it all. 

And it’s not just technical considerations. Coordinating payments in different regions requires setting up individual legal entities and corresponding bank accounts in each region. Every region has different regulatory requirements, and each provider has a slightly different procedure for settling funds. Paddle’s legal and financial teams are involved every step of the way when rolling out a new payment destination and bear the cost of managing a more complex treasury.

## Looking to the future

The main thing we have planned for the future is to increase the number of merchant accounts held around the world. We’ve already made substantial investments in our payment routing solution which is already paying off, but there are still a few regions that represent a promising market for digital products that we’ve not yet expanded into. With the technical investments made, we have a launchpad from which to grow. The next challenge is building out the legal and financial structures required.  


We are also planning to increase our analytical modelling capabilities with some machine-learning techniques. Our approach up until recently has been to run relatively straightforward small-scale A/B tests on simple hypotheses, and then to adjust the rules accordingly. Developing more sophisticated models that use large amounts of historical test data would allow us to deploy much more complex rules that consider many more dimensions than we have today. 

It’s an exciting prospect with some interesting engineering challenges in store and we’ll be sure to share our progress along the way! With a unified payment lifecycle, we’re able to standardize payments from different PSPs, measure performance, and build a rules engine that determines how each payment gets routed. 

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)