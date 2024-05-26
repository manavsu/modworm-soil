export async function ReadRegisters(ip:string, port:number, func_code:number, address:number, count:number): Promise<string> {
    try {
        const request = `http://127.0.0.1:5000/rregs/${ip}/${port}/${func_code}/${address}/${count}`
        console.log('Request:', request);
        const response = await fetch(request, { method: 'GET' });
        if (!response.ok) throw new Error(`http error, status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

