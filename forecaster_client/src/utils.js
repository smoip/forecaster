export default {
  // not an ideal solution - this client should probably run its own tiny
  // backend to handle things like environment variables
  apiKey () {
    // replace me with serverless generated API key
    return "abc-123"
  },

  apiUrl () {
    // replace me with serverless generated API 'fetch_forecast' url
    return "https://example.amazonaws.com/some_stage/fetch_forecast"
  }
}
