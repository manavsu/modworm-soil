import { error } from '@sveltejs/kit';
import { BASE_URL } from "$lib/env";

export async function ReadRegisters(ip:string, port:string, func_code:number, address:number, count:number, data_type:number): Promise<string> {
    const response = await fetch(`${BASE_URL}/rregs/${ip}/${port}/${func_code}/${address}/${count}/${data_type}/`);
    console.log(response.status);
    if (!response.ok) error(response.status, await response.json());
    return await response.json();
}


