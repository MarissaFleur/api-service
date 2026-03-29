// types.ts
enum HttpMethod {
  GET = 'GET',
  POST = 'POST',
  PUT = 'PUT',
  DELETE = 'DELETE',
  PATCH = 'PATCH'
}

type ErrorResponse = {
  error: {
    status_code: number;
    message: string;
  };
}

type ParsedUrl = {
  protocol: string;
  hostname: string;
  pathname: string;
  search: string;
  hash: string;
}

type ServerError = {
  status_code: number;
  message: string;
}

type RoutingConfig = {
  path: string;
  method: HttpMethod;
  handler: Function;
  params?: string[];
  middlewares?: Function[];
}

type Request = {
  method: HttpMethod;
  headers: { [key: string]: string };
  body: any;
  query: { [key: string]: string };
  params: { [key: string]: string };
}

type Response = {
  status_code: number;
  body: any;
  headers: { [key: string]: string };
}