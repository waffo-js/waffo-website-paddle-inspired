---
title: "From legacy to leading: How we rebuilt Paddle for developers"
description: "After a decade of growth, Paddle's vision remained the same: to be the most intuitive and flexible billing platform and Merchant of Record. Here's how we tackled our technical debt and built a platform for our core users - developers."
source: "blog/how-we-rebuilt-paddle-for-developers.html"
---

# From legacy to leading: How we rebuilt Paddle for developers

![](https://images.prismic.io/paddle/Zq1DSUaF0TcGIqTV_Kieran.png?auto=format%2Ccompress&fit=max&w=384)

Author

[Kieran Mountford](/resources/author/kieran-mountford)

Senior Engineering Manager

Share

[](https://x.com/intent/tweet?text=From%20legacy%20to%20leading%3A%20How%20we%20rebuilt%20Paddle%20for%20developers%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fhow-we-rebuilt-paddle-for-developers%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fhow-we-rebuilt-paddle-for-developers)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fhow-we-rebuilt-paddle-for-developers&title=From%20legacy%20to%20leading%3A%20How%20we%20rebuilt%20Paddle%20for%20developers&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

In 2022, after a decade of growth and achieving a billion-dollar valuation, Paddle's vision remained the same: to be the most intuitive, powerful, and flexible billing platform on the market, all while handling tax, fraud, payment acceptance, and everything else involved with selling globally.

But we had to tackle the technical and product debt we’d accumulated with ten years of building. There was also a new focus for us: Delivering a world-class experience to those who will be working with our platform. 

As a result, we reimagined and rebuilt most of our core product and launched what we now call [**Paddle Billing**](https://www.paddle.com/billing).

## A short history of Paddle

In 2012, our founder, Christian Owens, launched Paddle to solve a problem he felt deeply when he launched his first successful project: Selling things online to a global audience was too complicated, especially if you were selling on MacOS. 

Paddle grew to become the de-facto licensing solution for Mac sellers and took the concept of a [Merchant of Record](https://www.paddle.com/blog/what-is-merchant-of-record) to a wider audience.

As we grew, our customers began asking for more support to sell Software as A Service (SaaS). Like all software before it, subscription billing was “eating the world” and our customers wanted more from Paddle to capitalize on this opportunity.

Whilst Paddle’s technology did what it should (we are a merchant of record that handles billions of dollars of revenue for our sellers after all), there was a _lot_ that could be improved especially for our technical customers.

  


## The challenge

Paddle already offered subscription functionality, and some customers were successfully running multi-million-dollar SaaS businesses with the platform. Evolving that functionality was the logical starting point and a subset of Paddle’s Product and Engineering team set out to do that. 

Unfortunately, estimates varied, goalposts moved, and little ground was gained on delivering the future of subscription functionality in a way that made sense for our sellers and for us.

At the same time, we were evaluating how to take that big step forward in our developer experience. It was evident that Paddle was a great product that solved a real need, but it was just as evident that our technical audience could be served much better. Our API was sub-standard, developer tooling was non-existent, and our developer documentation was not clear enough.

When you’re building a technical product to sell to technical people, you have to do better.   


## Building Paddle Billing with our customers in mind

![Exploring the fundamentals of the Paddle platform](https://images.prismic.io/paddle/Zq09QUaF0TcGIqR9_BuildingPaddleBillingimage.png?auto=format%2Ccompress&fit=max&w=3840)

Armed with over 15 years of combined Paddle knowledge, a few of us locked ourselves away in a room and started to examine where the platform was and where we wanted it to be.

As we were evaluating why previous attempts at evolving subscriptions weren’t achieving what we needed, it became evident that the scope of the task was bigger than just subscriptions. We found that there was a need to reimagine the platform from (almost) the ground up.  


### Start with the functionality to define the entities

With a task this big, we found we needed to strip it back to the fundamentals. We started by asking ourselves a few simple questions: “What are our customers trying to achieve?”, “How does our platform enable that?”, and “What do we expect to introduce over the next few years?”

Getting down what the product did, and having a clear view of what we – and our customers – wanted the product to _become_ , let us take our first step in defining the building blocks of the new platform. From a developer’s perspective, we were redefining Paddle’s**entities.**

We broke the answers to those questions down and simply began highlighting the nouns we needed to explore. For example:

  * A **customer** can complete a **transaction** to create a **subscription** for any number of **products** and **price** combinations.
  * A **subscription** can be paid for automatically via card or similar **payment methods** , or manually via an **invoice** and bank transfer (which is just another **payment method**).
  * A successful **payment** will result in a **completed** **transaction** providing all relevant information to our sellers.


This task at hand seems straightforward, but it’s a breakthrough to be able to break your product down like this. In my opinion, it’s rarely done this deliberately. especially in an established company. 

The outlines of these building blocks jump-started the next conversation and helped shape the underlying technical infrastructure, from services to data to the all-important API design.

Defining the structure of those entities was next, and UI / UX workshops or flow diagrams helped enormously here. What exactly is a customer? Or a price? We explored what data our users regularly worked with, what they’d likely want in the future, and what other considerations we needed to make. What data, for example, makes up a customer and how does that relate to payment methods, invoices, and reporting?

### Build for simplicity

The reality of every platform is that underneath this perceived complexity there is a set of pretty straight-forward building blocks that customers interact with. Most things, in most systems, can comfortably be boiled down to an API call and a data store update. There’s also beauty in the simplicity of REST. I understand not everything is a CRUD action on a simple entity, but so much can be done with that level of simplicity combined in interesting ways.

Equally, as developers, we’re used to understanding a platform via those entities and the actions we can take against those – so it’s fundamental to get these right. 

I also think we underestimate the impact we have here too. Entities are, or will become, _how your business talks about its platform_. From a simple idea of what a “price” is to what exactly we mean by a “transaction” or what the “adjustment report” gives customers. 

These entities are the language of the business as much as they are the language of the engineering team. Sometimes this will be business-led, other times it’s engineering teams who can – and should – shape these. [Domain Driven Design](https://www.oreilly.com/library/view/domain-driven-design-tackling/0321125215/) explores this concept in more detail than I will here.

The lesson we took away here is this: If you combine a clear understanding of your customers’ goals, and a deep focus on your platform’s core building blocks, your customers will be delighted when they interact with your product.

Whether it’s through a glossy UI or your API documentation, it will become so apparent to your customer that you understand their needs and offer a solution that’s _intuitive_ and _easy to work with_ when you get this right.

### Be API first

The result of all of the above work requires, but also feeds into, a culture within your product and engineering team of working API first. You must embrace all of the benefits (and of course, some drawbacks) of defining your features via an API spec and then going on to build them.

At Paddle, this is now the standard. We have an API Working Group that meets regularly to hear and discuss upcoming API changes, and we lint and enforce standards and consistency. It’s not a perfect way of working – I don’t believe one exists – but it’s enabled complex discussions to happen before any work begins and it’s allowed us to present a unified product and experience to our sellers.

### Build a team around your dev docs

**Your documentation is a critical product feature, and your most powerful sales tool.**

The final missing piece is documentation. Documentation isn’t a word that gets a lot of people excited, but if you’ve been paying attention to the software landscape it’s becoming increasingly obvious that it’s giving companies that invest in it a real edge.

When your customer base is made up of technical users, for them your documentation will be your most powerful marketing tool, your best onboarding guide, and your clearest sales message. Investing in your docs will _directly correlate_ with the positive appeal of your product, and successful go-live rate of your customers.

Your docs are a critical feature of your product and should be treated like one. Have a product manager assigned to your docs so they can understand your customer journey, have them talk to your commercial org about your ICP (Ideal Customer Profile), the information they want, and how to present it in a way that communicates the value of your product along that customer journey. Hire a writer who understands that developer documentation doesn’t have to be dry, and should convey the _value_ and the _why_ as much as the _how_.

We built a team around our documentation. We didn’t find an off-the-shelf platform we loved or that gave us the flexibility to achieve our goals, so we rolled our own as we built Billing out too. Build vs Buy is always a debate amongst product and engineering leadership with well-documented tradeoffs. For us, this turned out to be a great decision and we’re incredibly proud of the platform and the content we’ve put together on [developer.paddle.com](http://developer.paddle.com).

## We're ready for the what’s next 

At Paddle, we took a huge bet by making sweeping product and technical changes. We embarked on that journey guided by well-defined principles of what we wanted to achieve, and why, which made the decision-making process easier.

Since the launch of Paddle Billing, we’ve seen enormous improvements, both qualitatively and quantitatively, in how customers interact with the product. The shift in sentiment has been remarkable, due in large part to our focus on:

  1. Meeting our customers’ evolving needs with a product built for today’s subscription market, and for the years to come 
  2. Improving the experience for key technical decision makers through our API design, developer tooling, and thorough developer documentation.


These efforts not only addressed the current demands of global SaaS and digital product sellers, but also ensured our sellers are ready for whatever comes next.

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)