import { error } from '@sveltejs/kit';
import { BASE_URL } from "$lib/env";

export async function ReadRegisters(ip:string, port:string, func_code:number, address:number, count:number): Promise<string> {
    const response = await fetch(`${BASE_URL}/rregs/${ip}/${port}/${func_code}/${address}/${count}`);
    if (!response.ok) throw error(response.status, await response.json());
    return await response.json();
}
