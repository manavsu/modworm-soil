import { error} from '@sveltejs/kit';
import { BASE_URL } from '$lib/env';

export const ssr = false;

export async function load({ fetch, params }) {
	const port = params.port;
	const ip = params.ip;

	async function try_discover() {
		const response = await fetch(`${BASE_URL}/nmap/${ip}/${port}`);
		if (!response.ok) throw error(response.status, await response.json());
		const servers = await response.json();
	
		for (const server of servers) {
			if (server.address === ip && server.port === port) return true;
		}
		return false;
	}

	return { discovered: try_discover(), ip, port};
}



