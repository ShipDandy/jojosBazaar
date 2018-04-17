## ShipStation Custom Store Example

The purpose of this app is to illustrate the basic concepts of creating a custom store integration with ShipStation.

###### What is a Custom Store?

Custom stores allow for the building of a connection to ShipStation that helps automate the passing of order information. On the user's end an API endpoint is set up to act as an intermediary between their marketplace and ShipStation. The endpoint methods that a custom store user are responsible for creating should be able to respond to API requests from ShipStation with the presentation of order information or the ingestion of shipping information. Order information will be delivered and received using an XML format.

###### GET Requests

When the custom store endpoint is contacted with a GET request it should be able to provide new and updated orders based on the string parameter values of startDate and endDate passed in the call. Your backend system should query for orders with OrderDate and LastModified entries that fall within the time range established by startDate and endDate.

###### POST Requests

When an order has been shipped or fulfilled a shipment notification will be sent from ShipStation containing relevant shipment information such as:

* Carrier used
* Service used
* Tracking number associated

There may be cases where an order is shipped using methods not associated with a ShipStation carrier account. This is marking an order as shipped in ShipStation and will create a fulfillment. Shipment notification about this order will still be sent and information passed will depend upon what was included during the marking process.

###### Sidenote

In an actual production environment key aspects of this program like security and data management would be handled in a much more sophisticated manner.

###### Further Documentation

Additional information developing a custom store including a list of the tags accepted can be found at:

https://help.shipstation.com/hc/en-us/articles/205928478

###### About this app

This app is built using Python 3.6.5 and Flask module 0.12.2. Any similarity to order information both alive or dead is purely coincidental.