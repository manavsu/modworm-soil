import { error } from '@sveltejs/kit';

export async function ReadRegisters(ip:string, port:string, func_code:number, address:number, count:number): Promise<string> {
    const response = await fetch(`http://127.0.0.1:5000/rregs/${ip}/${port}/${func_code}/${address}/${count}`);
    console.log(`http://127.0.0.1:5000/rregs/${ip}/${port}/${func_code}/${address}/${count}`);
    if (!response.ok) throw error(response.status, await response.json());
    return await response.json();
}
