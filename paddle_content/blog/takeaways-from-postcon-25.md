---
title: "Key takeaways from POST/CON 25: APIs as AI infrastructure"
description: "Paddle Developer Advocate, Michael, shows why having strong API foundations is essential for using AI to enhance your platform - and more from POST/CON 25."
source: "blog/takeaways-from-postcon-25.html"
---

# Key takeaways from POST/CON 25: APIs as AI infrastructure

![Michael McGovern, Staff Developer Advocate](https://images.prismic.io/paddle/aHfHTkMqNJQqH-Zc_MichaelMcGovern.png?auto=format%2Ccompress&fit=max&w=1920)

Author

[Michael McGovern](/resources/author/michael-mcgovern)

Staff Developer Advocate

Share

[](https://x.com/intent/tweet?text=Your%20APIs%20are%20now%20AI%20infrastructure%3A%20takeaways%20from%20POST%2FCON%2025%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Ftakeaways-from-postcon-25%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Ftakeaways-from-postcon-25)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Ftakeaways-from-postcon-25&title=Your%20APIs%20are%20now%20AI%20infrastructure%3A%20takeaways%20from%20POST%2FCON%2025&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

Last month, our friends at [Postman](https://www.postman.com/) hosted [POST/CON 25](https://www.postman.com/postcon/2025/). It’s one of the biggest API conferences in the industry, gathering builders from PayPal, Hubspot, Salesforce, Zoom, and dozens of other thought leaders to talk about the future of APIs.

Of course, we couldn’t talk about the future without talking about AI. With the landscape shifting so quickly, we as API-first builders are all dealing with the same fundamental question: how do we build APIs in a world where our primary consumers might be AI agents, not human developers?

![From left to right: Postman Leaders from Zoom, Salesforce, Hubspot, P&G, NetDocuments, Paddle, Momento, PayPal. Abhinav Asthana \(center\) and Patricia Dugan \(far right\) from Postman.](https://images.prismic.io/paddle/aHptR0MqNJQqIG4O_leaders-group-photo.jpg?auto=format%2Ccompress&fit=max&w=3840)

Speaking with leaders from Postman, PayPal and Salesforce, and hearing unfiltered perspectives from leaders at AWS, Meta, and Decagon underscored a shift. **APIs have evolved from simple integration endpoints to become the execution layer of AI itself.**

## APIs as AI infrastructure

![Abhinav Asthana on the keynote stage at POST/CON.](https://images.prismic.io/paddle/aHpu0EMqNJQqIG48_postcon-keynote.jpg?auto=format%2Ccompress&fit=max&w=3840)

[Abhinav Asthana](https://www.linkedin.com/in/abhinavasthana/), the CEO and co-founder of Postman, set the scene [when he opened the keynote](https://www.youtube.com/watch?v=OHMxgRuW9H8). While there’s a lot of talk about AI, the foundational models are becoming interchangeable, and the real value is in connected systems. APIs are more important now than ever.

> Your APIs are no longer just integration endpoints. They’re the execution layer of AI."

[Abhinav Asthana](https://www.linkedin.com/in/abhinavasthana/), CEO and Co-Founder, Postman

This isn’t a product pitch, but reflects a fundamental transformation happening across the industry. For autonomous agents, APIs are crucial for converting thoughts into deterministic, high-quality actions.

It was evidenced everywhere at POST/CON. AI agents that gather customer context for support teams. Sales research agents that brief teams for outreach calls. Procurement agents that monitor software licenses autonomously.

This shift requires an evolution of the fundamentals of API design. The same APIs that power workflows built by humans must now [power AI agents](https://www.postman.com/product/ai-agent-builder/) that don’t think in the same way we do. When designing APIs, we need to consider that AI will struggle to interpret nuance or accurately fill in the blanks, knowing only what we’ve told them.

## Welcome to the messy middle - AI’s adolescence

![Keynote stage with Ankit Sobti from Postman, Srini Iragavarapu from AWS, Rangaprabhu Parthasarathy from Meta, and Sambhav Jain from Deacgon](https://images.prismic.io/paddle/aHpvIkMqNJQqIG5E_postcon-fireside-chat.jpg?auto=format%2Ccompress&fit=max&w=3840)

The [panel between leaders from AWS, Meta, and Decagon](https://www.youtube.com/watch?v=pHq5xQ_1DQc) had the perfect phrase for where we’re at today: “the messy middle.” We’re in a transition period, where we can see the power of AI but we’re not always perfectly connecting it to real use cases. Demos don’t cover edge cases, and models can seem to hallucinate randomly.

> This is the teenage phase [of AI]... raging hormones, so much energy, eventually these teens will grow up and solve real world problems.”

[Srini Iragavarapu](https://www.linkedin.com/in/isvas/), Director of Generative AI Applications and Developer Experiences, AWS

[Philippe Ozil](https://www.linkedin.com/in/philippeozil/) from Salesforce provided a perfect demonstration of this reality. During [his multi-agent systems talk](https://www.youtube.com/watch?v=PYH72TJ8ox8), his carefully orchestrated loan application workflow - featuring specialized agents for document verification, credit scoring, and risk analysis - simply wouldn't work. We’d chatted in the green room beforehand and he was super prepped, having refined his prompts and successfully rehearsed his demo countless times.

> It's really a trade-off between going fast, having something very flexible, very agile, and having something robust.”

[Philippe Ozil](https://www.linkedin.com/in/philippeozil/), Principal Developer Advocate, Salesforce

This wasn’t a failure of his presentation, but an authentic illustration of the messy middle. LLMs are generative in nature, so they can fail without us knowing why. And as Philippe remarked, “you can’t predict reliably what an AI agent is going to respond after using the same prompt 100 times.”

AI systems are powerful but unpredictable. They can upgrade tens of thousands of production applications (as AWS shared) or fail to retrieve a simple loan record (as the demo gods showed in Philippe’s demo), sometimes within the same system or workflow.

The panel revealed other messy realities involved with AI implementation:

  * We expect humans to make mistakes, but we expect computers to run instructions exactly. We hold AI to higher standards than humans.
  * When an AI doesn’t understand something, we can give it context. However, the risk of providing more information is the increase in so-called hallucinations.
  * For enterprise companies especially, the unpredictability of AI clashes with the organizational need for control. 


## Why being AI-ready matters

Even with all this unpredictability, the business case for AI is already undeniable. The panel shared compelling data on AI-driven workflows, with: 

  * developers seeing 45% productivity increases
  * customer support teams achieving 14% efficiency gains
  * sales teams reporting 17% higher revenue growth


> If you are trying to avoid experimenting with AI, you're going to regret it.”

[Rangaprabhu Parthasarathy](https://www.linkedin.com/in/rparthasarathy/), Director of GenAI, Meta

Amazon's example was particularly striking: they used AI to upgrade **30,000 production applications from one Java version to another, saving an estimated 4,500 years of engineering work**. But this success came because they already had the APIs and the infrastructure to adapt quickly.

The divide is becoming clear. Digital-native companies with solid API foundations are seeing immediate gains. More traditional companies with disparate systems and unclear API strategies are still in what the panel called the “experiment plus” phase.

At Paddle, we've witnessed this shift firsthand. When we replatformed from Paddle Classic to Paddle Billing, we built with API-first principles, not knowing that this would become the foundation for AI readiness. Having clear, well-documented APIs meant that we were able to [quickly bring Paddle into Claude and Cursor](https://developer.paddle.com/changelog/2025/paddle-mcp-ai-claude-cursor), and were one of the first to [embrace Postman’s suite of AI tools](https://paddle.getmcp.dev/).

Companies that skipped the API-first foundation are now playing catch-up on two fronts: building APIs and making them AI-ready.

## The framework: being a good AI citizen

![Rebecca from PayPal on stage delivering her paper. The slide behind is titled considerations for AI ready APIs.](https://images.prismic.io/paddle/aHpvgEMqNJQqIG5T_rebecca.jpg?auto=format%2Ccompress&fit=max&w=3840)

[Rebecca Hauck](https://www.linkedin.com/in/rebecca-hauck/) from PayPal summarized the most actionable insight that was weaved throughout the conference: “[being a good AI citizen.](https://www.youtube.com/watch?v=Tj8nGQMVK2k)” Just because you have APIs, doesn’t mean they’re automatically suitable for AI agents.

> If an API isn't well documented, an AI can't experiment like humans can."

[Rebecca Hauck](https://www.linkedin.com/in/rebecca-hauck/), Lead Technical Product Manager, PayPal

We’re all familiar with developer experience (DX), but it’s time to start thinking about agent experience (AX). Like developers, AI agents need clear documentation, good error handling, and consistency. But good AX also needs something more: rich metadata and relevant, contextual information that agents can't infer.

The overlap between DX and AX is something that resonates deeply with our experience at Paddle. Our API largely follows REST principles, but we have action endpoints for core use cases [like canceling subscriptions](https://developer.paddle.com/api-reference/subscriptions/cancel-subscription). While we could allow users to PATCH a subscription to cancel, an action endpoint is explicit in its intent and maps to natural language, serving both developers and AI agents.

## Building AI-ready APIs

Successful organizations aren’t waiting for AI to stabilize. They’re building the foundations now. 

Here are my thoughts about building AI-ready APIs from across the conference:

  * **Robust, consistent APIs are the foundation.**  
As the panel emphasized, everyone should be experimenting with AI. But experiments built on shaky API foundations lead to frustration, not insight.
  * **AI needs good docs.**   
The Postman team found that 43% of developers rely on colleagues to explain APIs. AI agents can’t do this. When your [API docs are machine-readable and always current](https://www.postman.com/product/spec-hub/), you're ready for whatever AI capabilities emerge next.
  * **Domain driven design isn’t just good engineering.**  
At Paddle, [rebuilding our platform forced us to redefine our entities](https://www.paddle.com/blog/how-we-rebuilt-paddle-for-developers) meaning that our API speaks the language of our customers. When AI agents encounter concepts like “subscriptions,” “customers,” or “proration,” they map to real business concepts, not abstract technical constructs.
  * **Build feedback loops.**  
The most striking insight from the [Decagon](https://decagon.ai/) team was how working with AI agents forced them to redesign customer APIs entirely. When agents started asking questions like “how many days left in my subscription?,” the existing APIs couldn't provide adequate responses.
  * **Plan for orchestration.**  
Philippe's multi-agent vision is exactly where we're heading. APIs that work in isolation won't be enough when AI agents need to coordinate [complex workflows across multiple services](https://www.postman.com/product/ai-agent-builder/).
  * **Enable confident experimentation.  
** Given the unpredictable nature of AI agents, you should limit what can go wrong when they inevitably do something unexpected. We recently [added granular permissions to the Paddle API](https://developer.paddle.com/changelog/2025/api-key-improvements), limiting the access that agents have.


## Your API foundations and the future

![Grid of four images. Image 1 is the POST/CON banner. Image 2 is Michael from Paddle laughing with the Postmanaut. Image 3 is Michael and Kieran from Paddle at the VIP reception. Image 4 is Justine from Postman on the keynote stage.](https://images.prismic.io/paddle/aHpvzkMqNJQqIG5e_postcon-wrapup.png?auto=format%2Ccompress&fit=max&w=3840)

POST/CON 25 was more than just a product keynote. It brought together practitioners from across industries grappling with the same challenges. Whether you're at PayPal optimizing for agent experience, at Salesforce building multi-agent workflows, or at Paddle designing billing APIs for an AI-first world, the questions are the same:

  * How do you build reliable systems on inherently unpredictable technology? 
  * How do you design for agents that can't improvise like humans? 
  * How do you balance the speed and flexibility AI promises with compliance and control?


Companies that embrace being good AI citizens, [designing APIs with agents as first-class consumers](https://www.postman.com/ai/ai-ready-apis/), are going to define the next era of software architecture. 

The foundations you build today will determine whether AI enhances your platform or bypasses it entirely. The question isn't whether AI will interact with your business, it's whether your business will be ready to interact with AI. The future belongs to the APIs that don't just serve AI, they enable it.

Explore the [Paddle API](https://god.gw.postman.com/run-collection/29428794-16aca740-3ad6-4c1a-97be-05dbc504b4c3?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D29428794-16aca740-3ad6-4c1a-97be-05dbc504b4c3%26entityType%3Dcollection%26workspaceId%3D5ed2587a-f47e-43e0-810c-0c3e782bca12#?env%5BSandbox%5D=W3sia2V5IjoiYmFzZVVybCIsInZhbHVlIjoiaHR0cHM6Ly9zYW5kYm94LWFwaS5wYWRkbGUuY29tIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImJlYXJlclRva2VuIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In1d) and [Paddle MCP server](https://paddle.getmcp.dev/) on the Postman API Network.

Interested in bringing Paddle into your AI workflows? [Sign up for more developer updates](https://developer.paddle.com/changelog/overview) \- no marketing emails, unsubscribe at any time.

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)