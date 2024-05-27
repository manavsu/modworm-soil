export async function ReadRegisters(ip:string, port:number, func_code:number, address:number, count:number): Promise<string> {
    try {
        const response = await fetch(`http://127.0.0.1:5000/rregs/${ip}/${port}/${func_code}/${address}/${count}`);
        if (!response.ok) throw new Error(`http error, status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export async function Nmap(ip:string, port:number) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/nmap/${ip}/${port}`)
        if (!response.ok) throw new Error(`http error, status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export async function VerifySlave(ip:string, port:number) {
    const response = await Nmap(ip, port);
    console.log(response);
    for (const i in response) {
        if (response[i].address === ip && response[i].port === port) {
            return true;
        }
    }
    return false;
}
        
