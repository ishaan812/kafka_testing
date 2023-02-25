package main

import (
	"encoding/json"
	"fmt"

	snowplowsdk "github.com/snowplow/snowplow-golang-analytics-sdk/analytics"
)

func ParseTSV(tsvString string) ([]byte, error) {
	event := `website	web	2023-02-24 09:59:34.701	2023-02-24 09:59:34.429	2022-10-10 10:42:34.151	unstruct	82dbf502-5731-4423-8eae-7090b78338a8		biz1	js-3.5.0	ssc-2.8.2-kafka	snowplow-enrich-kafka-3.7.0		127.0.0.1		85094061-f702-4b62-a46d-20f7226b4741	29	c29840a5-25b0-430c-8eb3-bfcb4ecd1431												https://snowplow.io/			https	snowplow.io	443	/																							{"schema":"iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0","data":{"schema":"iglu:com.nitiai/node_events_public/jsonschema/1-0-0","data":{"eventId":"4cdf6a87-d6e3-45bd-9fa6-22bbd90b0f4b","timestamp":"1676543492","eventType":"VIEWED","source":"SDK","userId":"b8243e0e-a025-4c15-918b-bc4cee008bda","flowId":"3b478ac6-a687-47c7-99ca-45a0089e93cc","nodeId":"56dceccf-9ddd-4505-93b3-44548a194af3","nodeLevel":"2","nodeOrder":"1","nodeName":"Stash Create Success","podId":"491807c9-1f4b-4bb1-8a5a-ba15759058db","cohortId":"8baa9da3-04df-4a21-b9f5-76ed4e9be6da"}}}																			curl/7.79.1						en-GB										1	30	693	1302				Europe/London			3440	1440	UTF-8	678	9015												2022-10-10 10:42:34.153				be9520e7-16a5-4d4e-afa1-8e269f99a1cf	2023-02-24 09:59:34.427	com.nitiai	node_events_public	jsonschema	1-0-0		`
	parsed, err := snowplowsdk.ParseEvent(event) // Where tsvString is a valid TSV string Snowplow event.
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	bytes, jsonErr := parsed.ToJson() // whole event to JSON
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return nil, jsonErr
	}
	// print(string(bytes))
	// parsed.ToMap()                                                                   // whole event to map
	// parsed.GetValue("page_url")                                                      // get a value for a single canonical field
	// parsed.GetSubsetMap("page_url", "domain_userid", "contexts", "derived_contexts") // Get a map of values for a set of canonical fields
	// parsed.GetSubsetJson("page_url", "unstruct_event")                               // Get a JSON of values for a set of canonical fields
	return bytes, nil
}

func WriteToDB(jsonBytes []byte) error {
	var event snowplowsdk.ParsedEvent
	json.Unmarshal(jsonBytes, event)
	fmt.Println(event)
	return nil
}

func main() {
	lol, _ := ParseTSV("")
	_ = WriteToDB(lol)

}
