function _success(result) {
  console.log('success:', result);
}

function _failure(error) {
  console.log('failure:', error);
}

function rpc(method, params, success, failure) {
  if (!success) success = _success;
  if (!failure) failure = _failure;
  url = '/server'
  rpcID = 1
  $.ajax({
    url:url,
    type:"POST",
    data:JSON.stringify({
      'jsonrpc': '2.0',
      'method': method,
      'params': params,
      'id': rpcID
    }),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(data) {
      if (data.error) {
        failure(data.error);
      } else {
        success(data.result);
      }
    }
  })
}

$(function() {
  console.log('hello, world!')
  rpc('testRPC', [1, 2])
});
