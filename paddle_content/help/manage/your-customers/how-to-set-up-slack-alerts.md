---
title: "How to set up Slack Alerts - Help Center - Paddle"
description: "How to set up Slack Alerts in Paddle  You can set up Slack Alerts for your subscriptions transactions payment attempts and new customers in Paddle via Relaya"
source: "help/manage/your-customers/how-to-set-up-slack-alerts.html"
---

# How to set up Slack Alerts - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Manage](/help/manage)[Your customers](/help/manage/your-customers)

How to set up Slack Alerts

# How to set up Slack Alerts with Relay.app

You can set up Slack Alerts for your subscriptions, transactions, payment attempts and new customers in Paddle via [Relay.app](https://www.relay.app/).

_We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _,_[__https://relay.app__](https://relay.app) _)_

_In this documentation, you can find all the below instructions:_

  * Set up alerts for Paddle in Slack
  * Set up alerts in Slack for all new Subscriptions
  * Set up alerts in Slack when a Subscription is canceled
  * Set up alerts in Slack for all new Transactions
  * Set up alerts in Slack for all Transactions under a certain price
  * Set up alerts in Slack for all Transactions over a certain price
  * Set up alerts in Slack when there is a failed Payment Attempt


  


## Set up alerts for Paddle in Slack

You can set up alerts for Paddle in Slack for a number of events including:

  * New Subscriptions

  * Subscription Cancellations

  * New Transactions

  * New Transactions under a certain price threshold

  * New Transactions over a certain price threshold

  * New Payment Attempts


 _Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

In this example we’ll show how to set up alerts for all new Subscriptions. 

1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”

4\. Select the event you’d like to alert on. In this example, we select “New subscription added” as the Trigger.

5\. If prompted, connect Paddle to Relay.app. You will also be asked whether you 'd like to connect your production or sandbox account.

6\. Then, you’ll be able to see relevant preview data in the Preview section of the step. In this example, we can see Subscription data in the Preview section of the “New subscription added” step.

7\. Now, we’ll add a step to send a notification in Slack for this event.

8\. Click “Add step” and type to filter for “Slack.” Select “Send message.”

9\. If prompted, connect Slack.

10\. Configure the Slack message:

11\. Select if you’d like to send the message to a Channel or a DM.

12\. Insert Subscription data by clicking on the + Data button below the text box or by using the @ syntax.

13\. Hover over the Subscription object to see the data fields that are available

14\. Select the data item or category you’d like to include in the Slack message. 

There are many other fields that could be used too, including:

  * Items included in the Subscription

  * Date the Customer will be charged next for this Subscription

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Currency Code

  * Date the Customer was first billed at


15\. Format the message by typing in plain text and include additional data points.

16\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. 

17\. When you hit “Test”, it will send a Slack message with this preview data. 

18\. Turn on the trigger.

You’re all set! 

  


## Set up alerts in Slack for all new Subscriptions

Here’s how to set up alerts for all new subscriptions. This is often the same as setting up an alert for all new customers.

_Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “New subscription added” as the trigger

5\. If prompted, connect Paddle to Relay.app

6\. Then, you’ll be able to see recent subscription data in the Preview section of the “New subscription added” step.

7\. Now, we’ll add a step to send a notification in Slack for this event.

8\. Click “Add step” and type to filter for “Slack.” Select “Send message.”

9\. If prompted, connect Slack.

10\. Configure the Slack message:

11\. Select if you’d like to send the message to a Channel or a DM.

12\. Insert Subscription data by clicking on the + Data button below the text box or by using the @ syntax. 

13\. Hover over the Subscription object to see the data fields that are available

14\. Select the data item or category you’d like to include in the Slack message. This example pulls the Customer Name. 

There are many other fields that could be used too, including:

  * Items included in the Subscription

  * Date the Customer will be charged next for this Subscription

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Currency Code

  * Date the Customer was first billed at


15\. Format the message by typing in plain text and include additional data points.

16\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. 

When you hit “Test”, it will send a Slack message with preview data. 

17\. Turn on the trigger

You’re all set! 

  


## Set up alerts in Slack when a Subscription is canceled

Here’s how you can set up alerts in Slack when a subscription is cancelled. This is often the same as when a customer churns.

_Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “Subscription changed” as the trigger

5\. Under “Fields to check for changes” select “Canceled at”

You’ll be able to see recent cancellations data in the Preview section. Now we’ll set up alerts for this event in Slack.

6\. Click “Add step” and type to filter for “Slack.” Select “Send message.”

7\. If prompted, connect Slack.

8\. Now, configure the Slack message:

9\. First, select if you’d like to send the message to a Channel or a DM.

10\. Insert data on the cancelled Subscription by clicking on the + Data button below the text box or by using the @ syntax. 

11\. Hover over the Subscription object to see the data fields that are available

12\. Select the data item or category you’d like to include. This example pulls the Customer Name. 

There are many other fields that could be used too, including:

  * Items included in the Subscription

  * Date the Customer will be charged next for this Subscription

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Currency Code

  * Date the Customer was first billed at


13\. Format the message by typing in plain text and include additional data points. In this example, we’re pulling the Customer Name and Customer Email.

14\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. When you hit “Test”, it will send a Slack message with this preview data. 

15\. Turn on the trigger

You’re all set!

  


## Set up alerts in Slack for all new Transactions

Use Relay.app to set up alerts in Slack for all new Paddle Transactions. 

 _Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

  


1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “New transaction added” as the trigger.

5\. You’ll be able to see recent transaction data in the Preview section.

6\. Now, we’ll create alerts in Slack for this event.

7\. Click “Add step” and type to filter for “Slack.” Select “Send message.”

8\. If prompted, connect Slack

9\. Now, configure the Slack message:

10\. First, select if you’d like to send the message to a Channel or a DM.

11\. Insert subscription data by clicking on the + Data button below the text box or by using the @ syntax. 

12\. Hover over the Transaction object to see the data fields that are available

13\. Select the data item or category you’d like to include. 

There are many other fields that could be used too, including:

  * Discount, Earnings, Fee, Collection Mode, Currency Code, and Checkout URL

  * Items in the Transaction

  * Subscription if there is one (including the Items in the Subscription, the Date the Customer will be charged next for the Subscription, and the Subscription ID)

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and Date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Date the customer was first billed at


14\. Format the message by typing in plain text and include any additional data points.

15\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. When you hit “Test”, it will send a Slack message with this preview data. 

16\. Turn on the trigger

You’re all set!

  


## Set up alerts in Slack for all Transactions under a certain price

Use Relay.app to get notified in Paddle when there’s a new Transaction under a certain price. 

 _Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

  


1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “New transaction added” as the trigger

5\. You’ll be able to see recent transaction data in the Preview section.

6\. Select “Add Filter”

7\. Select “Total Price”

8\. Select “Less than” in the drop down menu.

9\. Type the desired maximum price. You’ll see the transactions preview updated to reflect the price you’ve listed

10\. Select “Add Step”

11\. Type to filter for Slack and select “Send message”

12\. If prompted, connect Slack.

13\. Now, configure the Slack message:

14\. First, select if you’d like to send the message to a Channel or a DM.

15\. Insert subscription data by clicking on the + Data button below the text box or by using the @ syntax. 

16\. Hover over the Transaction object to see the data fields that are available.

17\. Select the data item or category you’d like to include. This example pulls the Customer Name. There are many other fields that could be used too, including:

  * Discount, Earnings, Fee, Collection Mode, Currency Code, and Checkout URL

  * Items in the Transaction

  * Subscription if there is one (including the items in the Subscription, the Date the customer will be charged next for the Subscription, and the Subscription ID)

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Date the customer was first billed at


18\. Format the message by typing in plain text and include any additional data points.

19\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. When you hit “Test”, it will send a Slack message with this preview data. 

20\. Enable your Trigger

You’re all set!

  


## Set up alerts in Slack for all Transactions over a certain price

Use Relay.app to send Slack alerts for all Transactions in Paddle over a certain price. 

 _Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “New transaction added” as the trigger

5\. You’ll be able to see recent transaction data in the Preview section.

6\. Select “Add Filter”

7\. Select “Total Price”

8\. Select “Greater than” in the drop down menu.

9\. Type the desired minimum price. You’ll see the transactions preview updated to reflect the price you’ve listed

10\. Click “Add Step”. Type to filter for “Slack.” Select “Send message”.

11\. If prompted, connect Slack.

12\. Now, configure the Slack message:

13\. First, select if you’d like to send the message to a Channel or a DM.

14\. Insert Transaction data by clicking on the + Data button below the text box or by using the @ syntax. 

15\. Hover over the Transaction object to see the data fields that are available.

16\. Select the data item or category you’d like to include. This example pulls the Customer Name. There are many other fields that could be used too, including:

  * Discount, Earnings, Fee, Collection Mode, Currency Code, and Checkout URL

  * Items in the Transaction

  * Subscription if there is one (including the items in the Subscription, the Date the customer will be charged next for the Subscription, and the Subscription ID)

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and Date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Date the customer was first billed at


17\. Format the message by typing in plain text and include any additional data points.

18\. Click “Test this step”. This will open up a preview area where you can see the subscription the step will be tested with. When you hit “Test”, it will send a Slack message with this preview data. 

19\. Enable your workflow.

You’re all set!

  


## Set up alerts in Slack when there is a failed Payment Attempt

You can set up alerts in Slack when there is a failed Payment Attempt in Paddle using Relay.app. 

 _Note that the integration is powered by Relay.app (_[__https://relay.app__](https://relay.app) _).__We do not take any responsibility for the product and do not provide technical support for these plugins. For any questions or support needs, you will need to reach out to Relay support directly (_[__support@relay.app__](mailto:support@relay.app) _)_

1\. First, create an account on [_Relay.app_](https://relay.app)

2\. Then, hit the + button to create your first workflow.

3\. Click the “Add trigger” button and type to filter for “Paddle”.

4\. Select “New Payment added” as the Trigger

5\. Select “Add filter.”

6\. Select “Status.”

7\. Select “Unsuccessful payment attempt.”

You’ll see the payment attempt populate in the Preview panel if there are past unsuccessful payment attempts.

8\. Now, we’ll set up alerts in Slack when this event occurs. 

9\. Select “Add Step.”

10\. Type to filter for Slack and select “Send message.”

11\. If prompted, connect Slack.

12\. Now, configure the Slack message:

13\. Select if you’d like to send the message to a Channel or a DM.

14\. Insert subscription data by clicking on the + Data button below the text box or by using the @ syntax. 

15\. Hover over the Payment Attempt object to see the data fields that are available

Select the data item or category you’d like to include. This example pulls the Customer Name. There are many other fields that could be used too, including:

  * Time the payment attempt occurred

  * Discount, Earnings, Fee, Collection Mode, Currency Code, and Checkout URL

  * Items in the Transaction

  * Subscription if there is one (including the Items in the Subscription, the Date the customer will be charged next for the Subscription, and the Subscription ID)

  * Customer Address (including details of the City, Country Code, Postal Code, Region, and date the address was added) 

  * Business Name, Business Tax identifier, and the time the Business was added

  * Date the customer was first billed at


16\. Format the message by typing in plain text and include any additional data points.

17\. Click “Test this step”. This will open up a preview area where you can select a payment attempt from the past and test with this payment attempt. When you hit “Test”, it will send a Slack message with this preview data. 

18\. Enable your Trigger

You’re all set!