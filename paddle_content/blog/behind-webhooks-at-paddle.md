---
title: "Podcast: Behind webhooks at Paddle - Insights into event delivery at scale"
description: "From Black Friday Stress Test to Daily Scale - How we Built a Webhook System for Hypergrowth. A Podcast with Hookdeck's Phil Legetter"
source: "blog/behind-webhooks-at-paddle.html"
---

# Podcast: Behind webhooks at Paddle - Insights into event delivery at scale

![](https://images.prismic.io/paddle/aDczridWJ-7kSpYw_2174476.jpeg?auto=format%2Ccompress&fit=max&w=1080)

Author

[Michael Woodward](/resources/author/michael-woodward)

Share

[](https://x.com/intent/tweet?text=Behind%20webhooks%20at%20Paddle%3A%20Insights%20into%20event%20delivery%20at%20scale%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fbehind-webhooks-at-paddle%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fbehind-webhooks-at-paddle)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fbehind-webhooks-at-paddle&title=Behind%20webhooks%20at%20Paddle%3A%20Insights%20into%20event%20delivery%20at%20scale&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

Two years ago, Black Friday was our webhook delivery stress test. Today, we handle that same volume every single day. 

I recently sat down with [Phil Legetter](https://www.linkedin.com/in/leggetter/) at Hookdeck to discuss how we built infrastructure that scales with hypergrowth.

[Webhooks](https://developer.paddle.com/webhooks/overview) are automated messages sent from apps when important events happen. At Paddle, as a merchant of record processing millions of transactions, they’re business-critical for our customers. When a user signs up or cancels their subscription, webhooks make sure users get the correct access to the app immediately.

## Event-driven architecture at scale

Our event delivery system is built around thoughtfully designed architecture that handles both predictable daily traffic, and those unexpected spikes we all know and love.

One thing I emphasized in the conversation: “event delivery is extremely spiky.” This unpredictability drives many of our architectural decisions, from how we handle idempotency checks to our exponential backoff strategy for failed deliveries.

The part I’m especially proud of is our queue prioritization approach. When a webhook destination times out or returns an error, we don’t immediately retry through the same high-priority queue. Instead, retries get routed to a low-priority queue to prevent “noisy neighbor” problems. This way, one problematic destination won’t impact delivery performance for everyone else.

## Testing webhook flows end-to-end

One of my favorite projects has been our [webhook simulator](https://developer.paddle.com/webhooks/test-webhooks).

![](https://images.prismic.io/paddle/aDCKYydWJ-7kSgCq_webook-simulator.png?auto=format%2Ccompress&fit=max&w=3840)

Anyone who’s worked with purchases and subscriptions knows how complicated the flows can get. 

During a checkout, you're creating customers, payments, subscriptions, and testing all those event sequences manually can be tricky.

Our webhook simulator lets developers play complex event sequences from start to finish, using real data, so they can debug issues before going live.

In our conversation, I dive into several technical challenges we’ve solved:

  * Reliability: How we maintain “three nines” on our 2-second delivery SLO.
  * Concurrency: Our approach to distributed processing using Redis locks for idempotency.
  * Security: Implementation details of webhook verification and SDK support.
  * Scalability: Handling daily traffic on par with our Black Friday peaks from two years ago. 


## The bigger picture

Building reliable event delivery at scale presents unique challenges that go beyond typical API development. I tried to share both our architectural decisions and the real-world lessons we’ve learned along the way.

Whether you’re handling hundreds or millions of events, I hope some of these insights help with your own event-driven systems. Check out the full conversation to learn more. 

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)