package main

import (
	"fmt"
	"strings"

	"github.com/snowplow/snowplow-golang-analytics-sdk/tracker"
)

type RegisterEvent struct {
	UserId   string `json:"userId"`
	Username string `json:"username"`
	Email    string `json:"email"`
}

func main() {
	t := tracker.NewTracker("my-app", "1.0.0", "com.acme_company", "http://my-collector-url")
	line := "2023-02-14 10:30:15\tlocalhost\tGET\t200\thttps://example.com\tMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\t{\"schema\":\"iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0\",\"data\":{\"schema\":\"iglu:com.acme_company/register/jsonschema/1-0-0\",\"data\":{\"userId\":\"12345\",\"username\":\"johndoe\",\"email\":\"johndoe@example.com\"}}}"

	fields := strings.Split(line, "\t")
	payloadData := fields[len(fields)-1]
	payload, err := t.NewPayloadFromJSON(payloadData)
	if err != nil {
		panic(err)
	}

	registerEvent := RegisterEvent{}
	if err := payload.GetJSON("data", &registerEvent); err != nil {
		panic(err)
	}

	fmt.Printf("User ID: %s\n", registerEvent.UserId)
	fmt.Printf("Username: %s\n", registerEvent.Username)
	fmt.Printf("Email: %s\n", registerEvent.Email)
}
