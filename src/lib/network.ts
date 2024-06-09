export class Socket {
    address: string;
    port: string;

    constructor(address: string, port: string) {
        this.address = address;
        this.port = port;
    }
}

export class Network {
    cidr: string;
    ports: string;
    open_sockets: Socket[];

    constructor(cidr: string, ports: string, open_sockets: Socket[]) {
        this.cidr = cidr;
        this.ports = ports;
        this.open_sockets = open_sockets;
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    static fromJson(cidr: string, ports: string, json: any): Network {
        const sockets = [];
        for (const socket of json) {
            sockets.push(new Socket(socket.address, socket.port));
        }
        return new Network(cidr, ports, sockets);
    }
}