description = [[
Simple script to get HTTP server info
]]

author = "Srija"
license = "Same as Nmap"
categories = {"default", "safe"}

portrule = function(host, port)
    return port.number == 80 or port.number == 8080
end

action = function(host, port)
    local socket = nmap.new_socket()
    socket:connect(host.ip, port.number)

    socket:send("GET / HTTP/1.1\r\nHost: " .. host.ip .. "\r\n\r\n")

    local response = socket:receive_lines(10)
    socket:close()

    return response
end
