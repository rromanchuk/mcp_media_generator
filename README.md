# What is it?

A [Model Context Protocol](https://modelcontextprotocol.io/) Server running over SSE

# What it offers?

Tools to create images using Amazon Nova Canvas model and videos using Amazon Nova Reel model.

# What do I need?

- Amazon Bedrock account with access to Amazon Nova Canvas and Amazon Nova Reel models.
- Amazon S3 bucket to store the video
- MCP Client, such is Claude Desktop or [LibreChat](https://github.com/danny-avila/LibreChat)

# How to run this?

Using Docker with precompiled image as per docker-compose.yml. App is listening on port 8961.

## How to add to LibreChat

In your librechat.yaml file, add the following section:

```yaml
mcpServers:
  media-creator:
    type: sse # type can optionally be omitted
    url: URL of your docker container # e.g. http://localhost:8961/sse
```

## How to use in LibreChat

After the server is added to LibreChat as per above, restart LibreChat to connect to MCP server and discover tools. Then, create an agent and add the respective tools to agent.

When the agent is created, you may ask the agent to create image or video which should invoke the provided tools.
