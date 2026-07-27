# Error Handling

## **Error Handling**

### Common HTTP Status Codes

- **200:** Success

- **400:** Bad Request - Invalid parameters or operation not allowed

- **401:** Unauthenticated - Invalid or missing API key

### Error Response Format

All error responses follow a consistent format:

```json
{
  "status": 400,
  "message": "Error description"
}
```
